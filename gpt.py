from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

file = "post-history.txt"
# Ensure the file exists before trying to read it
if not os.path.exists(file):
    with open(file, 'w') as f:
        f.write("")

# Read the file content
with open(file, 'r') as f:
    post_history = f.read()

def chat_gpt(user_message):
    print(f"Post history: {post_history}")

    client = OpenAI(
        # This is the default and can be omitted
        api_key = os.getenv('OPENAI_API_KEY')
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f'''
                            You are a facebook social media manager for the travel agency 'Dube Travels'. 
                            Your responses must be different than your previous responses here: {post_history}''',
            },
            {
                "role": "user",
                "content": user_message,
            }
        ],
        model="gpt-3.5-turbo",
    )

    # Access the content using the 'message' attribute of the Choice object
    assistant_message = chat_completion.choices[0].message.content

    return assistant_message
