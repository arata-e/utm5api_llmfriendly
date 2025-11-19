import re
import json

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute
import uvicorn
import os
from functools import partial
# import httpx # Removed httpx

# Assuming parser.py is in the same directory
from parser import parse_markdown_file

app = FastAPI()

API_URL_PREFIX = "api"
# API_BASE_URL = os.getenv("UTM5_API_BASE_URL", "http://localhost:5000") # Removed API_BASE_URL

UTM5_MCP_SERVER_ID = "utm5-api-mcp"

# Store parsed API definitions globally
api_definitions = []

def load_api_definitions():
    global api_definitions
    markdown_files = [f for f in os.listdir('.') if f.endswith('.md') and f != 'README.md']
    for md_file in markdown_files:
        print(f"Parsing {md_file}...")
        parsed_data = parse_markdown_file(md_file)
        # Filter out endpoints where 'ready' is false
        ready_endpoints = [ep for ep in parsed_data["endpoints"] if ep["ready"] is True]
        if ready_endpoints:
            api_definitions.append({"section_name": parsed_data["section_name"], "endpoints": ready_endpoints})
    print("API Definitions Loaded.")

@app.on_event("startup")
async def startup_event():
    load_api_definitions()
    # create_dynamic_routes() # Dynamic routes will be replaced by MCP endpoints

# Dynamic route creation is no longer needed for MCP, it's about exposing metadata
# def create_dynamic_routes():
#     pass # This function will be removed or repurposed

@app.get("/")
async def read_root():
    return {"message": "UTM5 API Model Context Protocol Server. Visit /docs for OpenAPI spec, or use MCP tools to discover resources."}

@app.get("/list_mcp_resources")
async def list_mcp_resources_endpoint():
    resources = []
    # Add a special "overview" resource for the system description
    resources.append({
        "server": UTM5_MCP_SERVER_ID,
        "Context7-compatible library ID": "/utm5/System/Overview",
        "Title": "UTM5 System Overview",
        "Description": "General information about the UTM5 ISP billing system, its purpose, main entities, and their relationships.",
        "Code Snippets": 0,
        "Source Reputation": "High",
        "Benchmark Score": 100,
        "Ready": True
    })

    for section in api_definitions:
        for endpoint in section["endpoints"]:
            # Construct a Context7-compatible library ID for each endpoint
            # Example: /utm5/User/Get_user_data
            library_id = f"/utm5/{section['section_name'].replace(' ', '_')}/{endpoint['name'].replace(' ', '_')}"
            resources.append({
                "server": UTM5_MCP_SERVER_ID,
                "Context7-compatible library ID": library_id,
                "Title": endpoint["name"],
                "Description": endpoint["description"], # Use the extracted description
                "Code Snippets": 1 if endpoint["example_response"] else 0, # Assume 1 if example exists
                "Source Reputation": "Unknown",
                "Benchmark Score": 0,
                "Ready": endpoint["ready"]
            })
    return resources

@app.get("/fetch_mcp_resource")
async def fetch_mcp_resource_endpoint(server: str, uri: str):
    if server != UTM5_MCP_SERVER_ID:
        raise HTTPException(status_code=404, detail=f"Server {server} not found.")

    # Parse the URI to find the corresponding endpoint
    # Expected URI format: /utm5/{SectionName}/{EndpointName}
    uri_parts = uri.lstrip('/').split('/')
    if len(uri_parts) != 3 or uri_parts[0] != "utm5":
        raise HTTPException(status_code=400, detail="Invalid URI format. Expected /utm5/{SectionName}/{EndpointName}")
    
    requested_section_name = uri_parts[1].replace('_', ' ')
    requested_endpoint_name = uri_parts[2].replace('_', ' ')

    # Handle the special "System Overview" resource
    if requested_section_name == "System" and requested_endpoint_name == "Overview":
        return {
            "server": UTM5_MCP_SERVER_ID,
            "uri": uri,
            "Title": "UTM5 System Overview",
            "Description": "UTM5 is an ISP billing system. Its core purpose is to manage subscribers, services, tariffs, and payments for internet service providers. "
                           "Key entities include: \n\n" # Use markdown for better formatting
                           "- **Users**: Individuals or organizations subscribed to services.\n"
                           "- **Accounts**: Financial accounts associated with users, managing balances and payments.\n"
                           "- **Tariffs**: Defines pricing plans and service conditions.\n"
                           "- **Services**: Specific offerings like internet access, IPTV, etc., linked to tariffs.\n"
                           "- **Dealers**: Resellers or partners who manage their own set of users.\n\n"
                           "Relationships: Users can have multiple accounts, accounts are linked to services and tariffs, dealers manage users."
        }

    for section in api_definitions:
        if section["section_name"] == requested_section_name:
            for endpoint in section["endpoints"]:
                if endpoint["name"] == requested_endpoint_name:
                    # Return detailed documentation for the endpoint
                    # This can be a structured JSON or a formatted string
                    return {
                        "server": UTM5_MCP_SERVER_ID,
                        "uri": uri,
                        "Name": endpoint["name"],
                        "Method": endpoint["method"],
                        "URL": endpoint["url"],
                        "Description": endpoint["description"],
                        "Ready": endpoint["ready"],
                        "Authentication": {
                            "Type": "Cookie",
                            "Name": "token",
                            "Description": "Authentication is done by sending a 'token' cookie with the access token."
                        },
                        "Parameters": endpoint["parameters"],
                        "Example Response": endpoint["example_response"]
                    }
    raise HTTPException(status_code=404, detail=f"Resource {uri} not found on server {server}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
