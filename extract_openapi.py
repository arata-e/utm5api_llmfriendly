#!/usr/bin/env python3
"""Extract a conservative OpenAPI 3.1 document from the bundled UTM5 HTML docs.

The HTML is a generated documentation export, not a machine-readable API schema.
This extractor preserves examples and explicit parameter tables, but does not
promote example values into required fields or invent missing response schemas.
"""
from __future__ import annotations

import json
import hashlib
import re
from pathlib import Path
from urllib.parse import parse_qsl, urlsplit

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "UTM Rest API.html"
OUTPUT = ROOT / "openapi.yaml"
REPORT = ROOT / "openapi_coverage.md"


def load_json_example(raw: str):
    raw = re.sub(r"^HTTP/\d(?:\.\d)?\s+\d{3}[^\n]*\n", "", raw.strip())
    try:
        return json.loads(raw), None, None
    except (json.JSONDecodeError, TypeError) as exc:
        # Repair only common documentation placeholders, keeping the exact raw
        # source and strict-parser error attached to the operation.
        normalized = raw
        changes = []
        without_ellipsis_lines = re.sub(r"(?m)^(\s*)\.\.\.\s*,?\s*$", r"\1", normalized)
        without_inline_ellipsis = re.sub(r"\.\.\.(?=\s*\])", "", without_ellipsis_lines)
        if without_inline_ellipsis != normalized:
            normalized = without_inline_ellipsis
            changes.append("removed ellipsis placeholder")
        without_trailing_commas = re.sub(r",(\s*[}\]])", r"\1", normalized)
        if without_trailing_commas != normalized:
            normalized = without_trailing_commas
            changes.append("removed trailing commas")
        if changes:
            try:
                return json.loads(normalized), str(exc), "; ".join(changes)
            except (json.JSONDecodeError, TypeError):
                pass
        return None, str(exc), None


def json_schema(value):
    """Infer a permissive schema from every value in the supplied example."""
    return schema_for_values([value])


def schema_for_values(values):
    if not values:
        return {}
    if all(isinstance(v, dict) for v in values):
        keys = set().union(*(v.keys() for v in values))
        return {
            "type": "object",
            "properties": {str(k): schema_for_values([v[k] for v in values if k in v]) for k in sorted(keys)},
            "additionalProperties": True,
        }
    if all(isinstance(v, list) for v in values):
        members = [item for array in values for item in array]
        return {"type": "array", "items": schema_for_values(members)}

    types = set()
    for value in values:
        if value is None:
            types.add("null")
        elif isinstance(value, bool):
            types.add("boolean")
        elif isinstance(value, int):
            types.add("integer")
        elif isinstance(value, float):
            types.add("number")
        elif isinstance(value, str):
            types.add("string")
        elif isinstance(value, dict):
            types.add("object")
        elif isinstance(value, list):
            types.add("array")
    if "number" in types and "integer" in types:
        types.discard("integer")
    if len(types) == 1:
        kind = next(iter(types))
        if kind == "object":
            return schema_for_values([v for v in values if isinstance(v, dict)])
        if kind == "array":
            return schema_for_values([v for v in values if isinstance(v, list)])
        return {"type": kind}
    schemas = []
    for kind in sorted(types):
        if kind == "object":
            schemas.append(schema_for_values([v for v in values if isinstance(v, dict)]))
        elif kind == "array":
            schemas.append(schema_for_values([v for v in values if isinstance(v, list)]))
        elif kind == "integer" and "number" in types:
            continue
        else:
            schemas.append({"type": kind})
    return {"anyOf": schemas}


def add_documented_fields(schema, fields):
    """Add explicitly tabulated success fields to object-shaped sample schemas."""
    kind = schema.get("type")
    if kind == "array":
        schema["items"] = add_documented_fields(schema.get("items", {}), fields)
    elif "anyOf" in schema:
        object_variants = [i for i, variant in enumerate(schema["anyOf"]) if variant.get("type") == "object"]
        if object_variants:
            for i in object_variants:
                schema["anyOf"][i] = add_documented_fields(schema["anyOf"][i], fields)
        else:
            schema["anyOf"].append(add_documented_fields({}, fields))
    elif kind in (None, "object"):
        schema["type"] = "object"
        properties = schema.setdefault("properties", {})
        for field in fields:
            name = field["name"]
            documented = {**field["schema"], "description": field["description"]}
            observed = properties.get(name)
            if observed and observed.get("type") and documented.get("type") and observed["type"] != documented["type"]:
                observed_types = {observed["type"], documented["type"]}
                if observed_types <= {"integer", "number"}:
                    documented["type"] = "number"
                else:
                    variants = observed.get("anyOf", [observed])
                    documented_variants = documented.get("anyOf", [documented])
                    documented = {
                        "anyOf": variants + [v for v in documented_variants if v not in variants],
                        "description": field["description"],
                        "x-doc-status": "source-example-type-conflict",
                        "x-source-type": field["type"],
                    }
            if documented:
                properties[name] = documented
        schema.setdefault("additionalProperties", True)
    return schema


def scalar_type(raw: str):
    t = raw.strip().lower()
    if t in {"number", "integer", "int"}:
        return {"type": "integer" if t != "number" else "number"}
    if t in {"boolean", "bool"}:
        return {"type": "boolean"}
    if t in {"string", "date", "datetime"}:
        return {"type": "string"}
    return {}


def get_table_fields(article):
    result = []
    for table in article.select("table"):
        rows = table.select("tr")
        if not rows:
            continue
        headers = [c.get_text(" ", strip=True).lower() for c in rows[0].find_all(["th", "td"], recursive=False)]
        # The source labels columns in Russian; each row is Name, Type, Description.
        for row in rows[1:]:
            cells = [c.get_text(" ", strip=True) for c in row.find_all(["th", "td"], recursive=False)]
            if len(cells) < 2:
                continue
            name = cells[0]
            typ = cells[1]
            desc = cells[2] if len(cells) > 2 else ""
            if not name:
                continue
            heading = table.find_previous(["h2", "h3"])
            section = heading.get_text(" ", strip=True).lower() if heading else ""
            result.append({"name": name, "type": typ, "description": desc, "section": section})
    return result


def extract():
    soup = BeautifulSoup(SOURCE.read_text(encoding="utf-8"), "html.parser")
    paths = {}
    operations = []
    seen_operation_ids = set()
    for article in soup.select("article[data-group][data-name]"):
        url_node = article.select_one('pre[data-type] code.language-http')
        if not url_node:
            continue
        raw_url = url_node.get_text("", strip=True)
        parsed_url = urlsplit(raw_url)
        path = parsed_url.path
        if not path.startswith("/"):
            path = "/" + path
        method = (article.get("data-type") or "").lower()
        if not method:
            method_node = article.select_one("span.type")
            method = method_node.get_text(" ", strip=True).lower() if method_node else ""
        method = method.replace("type__", "")
        title_node = article.select_one("h1")
        title = title_node.get_text(" ", strip=True) if title_node else article.get("data-name", "")
        title = re.sub(r"\s+", " ", title)
        group = article.get("data-group", "Other")
        hidden = "hide" in (article.get("class") or [])
        opid_base = re.sub(r"[^A-Za-z0-9]+", "_", f"{group}_{article.get('data-name', title)}").strip("_")
        opid = re.sub(r"[^A-Za-z0-9_]", "", opid_base)
        if opid in seen_operation_ids:
            suffix = hashlib.sha1(f"{method}:{path}".encode()).hexdigest()[:8]
            opid = f"{opid}_{suffix}"
        seen_operation_ids.add(opid)
        params = []
        body_fields = []
        response_fields = []
        header_fields = []
        for item in get_table_fields(article):
            schema = scalar_type(item["type"])
            field = {"type": item["type"], "description": item["description"], "schema": schema}
            req_match = re.search(r"\bnot required\b|\boptional\b", item["description"], re.I)
            requiredness = "documented-optional" if req_match else "undocumented"
            section = item["section"]
            if "success" in section or "error" in section or re.match(r"\d{3}", section):
                response_fields.append({**field, "name": item["name"]})
            elif "body" in section or "request body" in section:
                body_fields.append({**field, "name": item["name"]})
            elif "header" in section:
                header_fields.append({**field, "name": item["name"]})
            elif "request body" in item["description"].lower():
                # A few source tables place uploads under Parameters but explicitly
                # describe the field as part of the request body.
                if item["type"].lower() == "object" and "file" in item["name"].lower():
                    field["schema"] = {"type": "string", "format": "binary"}
                    field["media_type"] = "multipart/form-data"
                body_fields.append({**field, "name": item["name"]})
            else:
                location = "query"
                params.append({
                    "name": item["name"], "in": location, "required": False,
                    "description": (item["description"] or f"Source type: {item['type']}") + ("" if req_match else " Requiredness is not stated in the source."),
                    "schema": schema or {},
                    "x-requiredness": requiredness,
                    **({"x-source-type": item["type"]} if not schema else {}),
                })
        for item in header_fields:
            optional = bool(re.search(r"\bnot required\b|\boptional\b", item["description"], re.I))
            params.append({"name": item["name"], "in": "header", "required": False,
                          "description": (item["description"] or f"Source type: {item['type']}") + ("" if optional else " Requiredness is not stated in the source."),
                          "schema": item["schema"] or {},
                          "x-requiredness": "documented-optional" if optional else "undocumented",
                          **({"x-source-type": item["type"]} if not item["schema"] else {})})
        # Query strings shown in the documented usage example are explicit evidence.
        for code in article.select("pre code"):
            txt = code.get_text("", strip=True)
            if not re.match(r"^(?:https?://|/api/|api/)", txt, re.I):
                continue
            query = urlsplit(txt).query
            for name, _ in parse_qsl(query, keep_blank_values=True):
                if not any(p["name"] == name and p["in"] == "query" for p in params):
                    params.append({"name": name, "in": "query", "required": False,
                                   "description": "Observed in the source usage example; type/requiredness are undocumented.",
                                   "schema": {}, "x-doc-status": "inferred-from-example"})

        req_example = None
        req_error = None
        req_normalized = None
        req_raw = None
        for pane in article.select(".tab-pane"):
            pane_id = pane.get("id", "")
            if "parameter-examples" in pane_id or "request-example" in pane_id.lower():
                code = pane.select_one("pre code.language-json")
                if code:
                    candidate = code.get_text().strip()
                    # The source marks some URL usage snippets as language-json.
                    # They are not request bodies; query parameters are extracted
                    # separately from all documented URL examples above.
                    if re.match(r"^(?:https?://|/api/|api/)", candidate, re.I):
                        continue
                    req_raw = code.get_text()
                    req_example, req_error, req_normalized = load_json_example(candidate)
                    break
        response_example = None
        response_error = None
        response_normalized = None
        response_raw = None
        for pane in article.select(".tab-pane"):
            if "success-examples" in pane.get("id", ""):
                code = pane.select_one("pre code")
                if code:
                    response_raw = code.get_text()
                    response_example, response_error, response_normalized = load_json_example(code.get_text())
                    break

        op = {
            "operationId": opid,
            "summary": title,
            "description": f"Source: UTM Rest API.html, group {group}, name {article.get('data-name')}, version {article.get('data-version', 'unknown')}. "
                           "Requiredness and schemas are only stated where the source documents them.",
            "tags": [group],
            "parameters": params,
            "responses": {},
            "x-source": {"file": "UTM Rest API.html", "group": group,
                         "name": article.get("data-name"), "version": article.get("data-version", "unknown"),
                         "hidden": hidden, "article_id": article.get("id"),
                         "url": f"https://www.netup.ru/ru/utm5/utm5docs/5.5-026-release-rest/index.html#{article.get('id', '')}"},
        }
        if group == "Login" and method == "post" and path.rstrip("/") == "/api/login":
            # Login creates the temporary cookie session; it must not require
            # either of the credentials it is designed to establish.
            op["security"] = []
        if req_example is not None or body_fields:
            request_schema = json_schema(req_example) if req_example is not None else {"type": "object", "properties": {}}
            if body_fields:
                request_schema.setdefault("properties", {})
                for field in body_fields:
                    request_schema["properties"][field["name"]] = {**field["schema"], "description": field["description"]}
                request_schema["additionalProperties"] = True
            body_media_type = "multipart/form-data" if any(f.get("media_type") == "multipart/form-data" for f in body_fields) else "application/json"
            op["requestBody"] = {
                "required": False,
                "description": ("Source documents a file upload in the request body; multipart encoding is inferred from the file field." if body_media_type == "multipart/form-data" else "Request example from source. Schema is inferred from this example and does not establish required fields."),
                "content": {body_media_type: {"schema": request_schema}},
                "x-requiredness": "undocumented",
            }
            if req_example is not None:
                op["requestBody"]["content"][body_media_type]["example"] = req_example
            op["requestBody"]["x-doc-status"] = ("source-fields-and-normalized-example" if body_fields and req_normalized else ("normalized-example" if req_normalized else ("source-fields-and-example" if body_fields and req_example is not None else ("source-fields" if body_fields else "example-only"))))
            if req_normalized:
                op["x-source-request-example-error"] = req_error
                op["x-source-request-example-normalization"] = req_normalized
                op["x-source-request-example-raw"] = req_raw
            elif req_error:
                op["x-source-request-example-error"] = req_error
                op["x-source-request-example-raw"] = req_raw
        elif req_error:
            op["requestBody"] = {
                "required": False,
                "description": "The source includes a JSON request example, but it could not be parsed; inspect the retained raw example.",
                "content": {"application/json": {"schema": {}}},
                "x-doc-status": "incomplete",
                "x-requiredness": "undocumented",
            }
            op["x-source-request-example-error"] = req_error
            op["x-source-request-example-raw"] = req_raw
        if response_example is not None:
            response_schema = json_schema(response_example)
            if response_fields and isinstance(response_example, (dict, list)):
                response_schema = add_documented_fields(response_schema, response_fields)
            response = {"description": "Successful response (example in source).",
                        "content": {"application/json": {"schema": response_schema, "example": response_example}}}
            response["x-doc-status"] = ("source-fields-and-normalized-example" if response_fields and response_normalized else ("normalized-example" if response_normalized else ("source-fields-and-example" if response_fields else "example-only")))
            op["responses"]["200"] = response
            if response_normalized:
                op["x-source-response-example-error"] = response_error
                op["x-source-response-example-normalization"] = response_normalized
                op["x-source-response-example-raw"] = response_raw
        elif response_error:
            response = {"description": "Successful response; source example is not valid JSON.",
                        "content": {"application/json": {"schema": {}}},
                        "x-source-example": "invalid-json", "x-doc-status": "source-fields-with-invalid-example" if response_fields else "incomplete"}
            if response_fields:
                response["content"]["application/json"]["schema"] = {"type": "object", "properties": {
                    f["name"]: {**f["schema"], "description": f["description"]} for f in response_fields}}
            op["responses"]["200"] = response
            op["x-source-response-example-error"] = response_error
            op["x-source-response-example-raw"] = response_raw
        elif response_fields:
            op["responses"]["200"] = {
                "description": "Successful response; fields documented in source table.",
                "content": {"application/json": {"schema": {
                    "type": "object",
                    "properties": {f["name"]: {**f["schema"], "description": f["description"]} for f in response_fields},
                    "additionalProperties": True,
                }}},
                "x-doc-status": "source-fields",
            }
        else:
            op["responses"]["200"] = {"description": "Successful response; response body is not documented."}
        op["responses"].setdefault("4XX", {"description": "Client error; status codes and error payload schema are not documented in the bundled API source."})
        op["responses"].setdefault("default", {"description": "Error response; schema is not documented in source."})
        if not params:
            op.pop("parameters")
        paths.setdefault(path, {})[method] = op
        operations.append({"path": path, "method": method.upper(), "operationId": opid,
                           "title": title, "group": group, "hidden": hidden,
                           "params": len(params), "request": req_raw is not None,
                           "request_invalid": req_error is not None and not req_normalized,
                           "request_normalized": req_normalized,
                           "response": response_example is not None,
                           "response_invalid": response_error is not None and not response_normalized,
                           "response_normalized": response_normalized,
                           "source_version": article.get("data-version", "unknown")})
    return paths, operations


def yaml_dump(data):
    # PyYAML is available in the working environment. Keep deterministic ordering.
    import yaml

    class OpenAPIDumper(yaml.SafeDumper):
        def represent_str(self, value):
            # YAML 1.1 parsers disagree on numeric-looking strings with leading
            # zeroes. Quote them so sample identifiers remain strings everywhere.
            if re.fullmatch(r"[-+]?0[0-9]+(?:\.[0-9]+)?", value):
                return self.represent_scalar("tag:yaml.org,2002:str", value, style="'")
            return super().represent_str(value)

    OpenAPIDumper.add_representer(str, OpenAPIDumper.represent_str)
    return yaml.dump(data, Dumper=OpenAPIDumper, allow_unicode=True, sort_keys=False, width=110)


def main():
    paths, ops = extract()
    spec = {
        "openapi": "3.1.0",
        "info": {"title": "UTM5 REST API", "version": "5.5-026",
                 "description": "Generated conservatively from the bundled UTM5 REST API HTML export. See openapi_coverage.md for limitations and source coverage."},
        "servers": [{"url": "{scheme}://{host}", "description": "Set these variables to the target UTM5 deployment host and scheme.",
                     "variables": {"scheme": {"enum": ["http", "https"], "default": "http"},
                                   "host": {"default": "localhost", "description": "Host and optional port, for example utm5.example.net:8080"}}}],
        "security": [{"UTM5SessionCookie": []}, {"UTM5PermanentTokenCookie": []}],
        "components": {"securitySchemes": {
            "UTM5SessionCookie": {"type": "apiKey", "in": "cookie", "name": "session_id",
                                  "description": "Temporary session cookie. Obtain its value from POST /api/login; send it on each authenticated request.",
                                  "x-documentation": [
                                      "https://www.netup.ru/ru/utm5/utm5docs/5.5-024-release-web-pdf/documentation.pdf",
                                      "https://www.netup.ru/ru/utm5/utm5docs/5.5-033-release-web/index.html"]},
            "UTM5PermanentTokenCookie": {"type": "apiKey", "in": "cookie", "name": "token",
                                         "description": "Permanent token configured for a system user in the administrator web interface; send it on each authenticated request.",
                                         "x-documentation": [
                                             "https://www.netup.ru/ru/utm5/utm5docs/5.5-024-release-web-pdf/documentation.pdf",
                                             "https://www.netup.ru/ru/utm5/utm5docs/5.5-033-release-web/index.html"]}},
        },
        "tags": [{"name": name, "description": f"API operations for the {name} section."}
                 for name in sorted({o['group'] for o in ops})],
        "paths": paths,
    }
    OUTPUT.write_text(yaml_dump(spec), encoding="utf-8")
    rows = ["# OpenAPI extraction coverage", "",
            "Generated by `python3 extract_openapi.py` from `UTM Rest API.html`.", "",
            "Schemas inferred from examples describe observed values only; they do not define required fields. `x-requiredness: undocumented` means the OAS-required boolean is a placeholder and must not be treated as evidence that a field is optional. `x-doc-status` distinguishes example-only data from explicit table fields. Hidden source entries are retained and flagged in `x-source.hidden`.", "",
            f"Operations extracted: **{len(ops)}**; paths: **{len(paths)}**.", "",
            "| Group | Operations | Request examples | Response examples | Normalized response examples | Unparsed response examples | Hidden entries |", "|---|---:|---:|---:|---:|---:|---:|"]
    for group in sorted({o['group'] for o in ops}):
        subset = [o for o in ops if o['group'] == group]
        rows.append(f"| {group} | {len(subset)} | {sum(o['request'] for o in subset)} | {sum(o['response'] for o in subset)} | {sum(bool(o['response_normalized']) for o in subset)} | {sum(o['response_invalid'] for o in subset)} | {sum(o['hidden'] for o in subset)} |")
    rows += ["", "## Operations requiring follow-up", "",
             "All operations need a review of field requiredness and schema completeness. The status column identifies source examples requiring additional attention; authentication is described in the security schemes above.", "",
             "| Method | Path | Operation | Request example | Response example | Status |", "|---|---|---|---|---|---|"]
    for o in ops:
        status_parts = []
        if o['hidden']:
            status_parts.append("hidden source entry")
        if o['request_invalid']:
            status_parts.append("unparsed request example")
        if o['response_invalid']:
            status_parts.append("unparsed response example")
        if o['request_normalized'] or o['response_normalized']:
            status_parts.append("source example normalized")
        if not o['request'] and not o['response']:
            status_parts.append("no request or response example")
        elif not o['request']:
            status_parts.append("no request example")
        elif not o['response']:
            status_parts.append("no response example")
        if not status_parts:
            status_parts.append("review schema completeness and requiredness")
        status = "; ".join(status_parts)
        rows.append(f"| {o['method']} | `{o['path']}` | `{o['operationId']}` | {'yes' if o['request'] else 'no'} | {'invalid' if o['response_invalid'] else ('yes' if o['response'] else 'no')} | {status} |")
    rows += ["", "## Known limitations", "",
             "- Cookie authentication is sourced from official NetUP administrator guides (5.5-024 and 5.5-033); verify behavior against the exact deployed release if it differs from the API HTML export release (5.5-026).",
             "- Operation-level requiredness is not inferred from examples. Parameter-table fields are represented as optional until the source explicitly establishes requiredness.",
             "- Example-derived schemas are intentionally permissive and do not guarantee complete response/request contracts. Trailing commas and explicit ellipsis placeholders are repaired narrowly and marked with `x-source-*-example-normalization`.",
             "- Unparsed JSON response examples retain their raw source text in an `x-source-*-example-raw` extension and use an unconstrained JSON schema instead of a guessed payload shape.",
             "- Error status codes and error payload schemas are not invented; `default` is descriptive only.",
             "- `http://localhost` comes from examples and must be replaced for a deployment.", ""]
    REPORT.write_text("\n".join(rows), encoding="utf-8")
    print(f"Wrote {OUTPUT.name}: {len(ops)} operations, {len(paths)} paths")
    print(f"Wrote {REPORT.name}")


if __name__ == "__main__":
    main()
