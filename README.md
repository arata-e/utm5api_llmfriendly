# UTM5 REST API contract

`openapi.yaml` is the generated OpenAPI 3.1 description of the REST API documented in `UTM Rest API.html`. It is intended as a working contract for application development, with source coverage and known gaps recorded in [`openapi_coverage.md`](openapi_coverage.md).

## Regenerate

Requires Python 3, Beautiful Soup 4, and PyYAML:

```sh
python3 extract_openapi.py
```

The HTML export is the extraction source. The Markdown files and Postman collection are retained as cross-check material; the generator does not treat missing MD parameters or example-derived fields as proof that a contract is empty or complete.

## Use

The server host is configurable in the OpenAPI document. The bundled HTML examples use `http://localhost`; replace it with the address and scheme of the target UTM5 deployment before generating clients or sending requests. Paths include the `/api` prefix.

Operation schemas are conservative. Fields found in example payloads are represented as observed properties, but are not marked required unless the source establishes that. `x-doc-status` and `x-source` extensions identify example-derived contracts and their source entries. Unparsed JSON examples retain their source text in an extension and use an unconstrained JSON schema. Consult `openapi_coverage.md` for incomplete or malformed source examples.

The spec documents the two cookie methods described in NetUP administrator guides: temporary `session_id` from `POST /api/login` and a persistent system-user `token`. Those guides are versions 5.5-024 and 5.5-033, while the bundled API HTML is 5.5-026; confirm behavior against the exact deployed release.
