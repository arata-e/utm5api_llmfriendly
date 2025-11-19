import re
import json

def parse_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    section_match = re.search(r'# UTM5 API Section: (.*)', content)
    section_name = section_match.group(1).strip() if section_match else "Unknown Section"

    endpoints = []
    # Split the content by "## Endpoint:" to get individual endpoint blocks
    endpoint_blocks = re.split(r'## Endpoint: ', content)[1:]

    for block in endpoint_blocks:
        endpoint_name_match = re.match(r'(.*?)\n', block)
        endpoint_name = endpoint_name_match.group(1).strip() if endpoint_name_match else "Unknown Endpoint"

        method_match = re.search(r'- \*\*Method:\*\* `(.*?)`', block)
        method = method_match.group(1).strip() if method_match else "UNKNOWN"

        url_match = re.search(r'- \*\*URL:\*\* `{{api_url}}(.*?)`', block)
        url = url_match.group(1).strip() if url_match else "Unknown URL"

        ready_match = re.search(r'- \*\*Ready:\*\* `(.*?)`', block)
        ready = ready_match.group(1).strip().lower() == 'true' if ready_match else False

        endpoint_description_match = re.search(r'- \*\*Description:\*\* `(.*?)`', block)
        endpoint_description = endpoint_description_match.group(1).strip() if endpoint_description_match else "No description provided."

        parameters = []
        params_block_match = re.search(r'### Parameters:\n([\s\S]*?)(?:### Example Response:|$)', block)
        if params_block_match:
            params_text = params_block_match.group(1)
            param_matches = re.findall(r'- \*\*Name:\*\* `(.*?)`\s+- \*\*Type:\*\* `(.*?)`\s+- \*\*Description:\*\* (.*)', params_text)
            for name, type, description in param_matches:
                parameters.append({
                    "name": name.strip(),
                    "type": type.strip(),
                    "description": description.strip()
                })

        example_response_match = re.search(r'### Example Response:\s*```(?:\n|\r\n)([\s\S]*?)(?:\n|\r\n)```', block)
        example_response = {}
        if example_response_match:
            try:
                example_response = json.loads(example_response_match.group(1).strip())
            except json.JSONDecodeError:
                example_response = {"error": "Invalid JSON in example response"}

        endpoints.append({
            "name": endpoint_name,
            "method": method,
            "url": url,
            "ready": ready,
            "description": endpoint_description,
            "parameters": parameters,
            "example_response": example_response
        })
    return {"section_name": section_name, "endpoints": endpoints}

if __name__ == '__main__':
    # For testing, parse the User_api_llm_friendly.md file
    parsed_data = parse_markdown_file('User_api_llm_friendly.md')
    print(json.dumps(parsed_data, indent=2))
