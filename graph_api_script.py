import os 

import requests 

  

tenant_id = os.getenv("GRAPH_TENANT_ID") 

client_id = os.getenv("GRAPH_CLIENT_ID") 

client_secret = os.getenv("GRAPH_CLIENT_SECRET") 

  

token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token" 

  

data = { 

    "client_id": client_id, 

    "client_secret": client_secret, 

    "scope": "https://graph.microsoft.com/.default", 

    "grant_type": "client_credentials" 

} 

  

token_response = requests.post(token_url, data=data) 

token_json = token_response.json() 

  

#print("Token endpoint response:") 

#print(token_json) 

  

access_token = token_json.get("access_token") 

  

if not access_token: 

    print("Failed to obtain access token") 

    exit() 

  

headers = { 

    "Authorization": f"Bearer {access_token}" 

} 

  

graph_url = "https://graph.microsoft.com/v1.0/users" 

  

response = requests.get(graph_url, headers=headers) 

  

print("Graph response:") 

print(response.json())