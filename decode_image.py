import random

import requests
from base64 import b64decode
import json
import os

url = 'https://api.openai.com/v1/images/generations'
headers = {"Content-Type": "application/json",
           "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"}
data = {
    "prompt": "A pencil drawing of deadpool drawn like leonardo davinci",
    "response_format": "b64_json",
    "size": '256x256',
    "n": 1
}

response = requests.post(url, json=data, headers=headers)
res = response.json()["data"]  # [0]["url"]
urls = [res[x]["b64_json"] for x in range(len(res))]  # list of all images base64 encoding


def decode_image(b64_image_data_list: list):
    for base64 in b64_image_data_list:
        image_data = b64decode(base64)
        name = str(random.randrange(1, 1000)) + '.png'
        with open(name, 'wb') as png:
            png.write(image_data)
            print(f'{name} successfully decoded')


decode_image(urls)
print('--------done decoding----------')
