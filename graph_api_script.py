import os
import requests

# Read environment variables
tenant_id = os.getenv("GRAPH_TENANT_ID")
client_id = os.getenv("GRAPH_CLIENT_ID")
client_secret = os.getenv("GRAPH_CLIENT_SECRET")

# Microsoft Entra OAuth2 token endpoint
token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

# Request body
token_data = {
    "client_id": client_id,
    "client_secret": client_secret,
    "scope": "https://graph.microsoft.com/.default",
    "grant_type": "client_credentials"
}

# Request access token
token_response = requests.post(token_url, data=token_data)
token_json = token_response.json()

access_token = token_json.get("access_token")

if access_token:
    print("Access token acquired successfully")

    # Call Microsoft Graph API
    graph_url = "https://graph.microsoft.com/v1.0/users"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(graph_url, headers=headers)

    print("Graph API response:")
    print(response.json())

else:
    print("Failed to obtain access token")
    print(token_json)
