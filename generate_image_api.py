import os
import openai
import requests
URL = 'https://api.openai.com/v1/images/generations'
headers = {"Content-Type": "application/json",
"Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"}

data = {"prompt": "A pencil drawing of deadpool"}
response = requests.post(URL, json=data, headers=headers)
print(response.json())
