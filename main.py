import requests
from dotenv import load_dotenv
import os
from gpt import chat_gpt

load_dotenv()

page_access_token = os.getenv("PAGE_ACCESS_TOKEN")
page_id = os.getenv("PAGE_ID")

# URL for posting
url = f'https://graph.facebook.com/{page_id}/feed'

# Ensure post-history.txt file exists
file = "post-history.txt"
if not os.path.exists(file):
    with open(file, 'w') as f:
        f.write("")

# Generate the message using chat_gpt
message = chat_gpt(user_message="draft a post")

# Save the message to post history
with open(file, 'a') as f:
    f.write(f"-- Post History -- {message} -- Post History --\n")

# Data to be posted
data = {
    'message': message,
    'access_token': page_access_token
}

# Make the post request
response = requests.post(url, data=data)

# Check the response
if response.status_code == 200:
    print('Post successful!')
    print(response.json())
else:
    print('Failed to post.')
    print(response.json())
