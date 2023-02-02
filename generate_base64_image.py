import os
import requests

URL = 'https://api.openai.com/v1/images/generations'  # rest API endpoint
headers = {"Content-Type": "application/json",
           "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"}

data = {"prompt": "A pencil drawing of deadpool",
        "response_format": "b64_json",
        "size": '256x256'}


response = requests.post(URL, json=data, headers=headers)  # sending POST request
res = response.json()["data"][0]["b64_json"]
print(res[:50])
with open('b64.txt', 'w+') as temp:
    temp.write(res)  # write the base64 data to file.
