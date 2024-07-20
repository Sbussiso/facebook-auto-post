import requests
from dotenv import load_dotenv
import os

load_dotenv()

user_access_token = os.getenv("ACCESS_TOKEN")  # Ensure this is the user access token

# Get the page access token
url = 'https://graph.facebook.com/me/accounts'
params = {
    'access_token': user_access_token
}

response = requests.get(url, params=params)
if response.status_code == 200:
    print('Pages and tokens:')
    pages = response.json().get('data', [])
    if pages:
        for page in pages:
            print(f"Page Name: {page['name']}")
            print(f"Page ID: {page['id']}")
            print(f"Page Access Token: {page['access_token']}")
            if page['id'] == '354734874397464':  # Replace with your actual page ID
                page_access_token = page['access_token']
                with open('.env', 'a') as f:
                    f.write(f"\nPAGE_ACCESS_TOKEN={page_access_token}\n")
    else:
        print('No pages found or the user does not have admin access to any pages.')
else:
    print('Failed to retrieve pages and tokens.')
    print(response.json())