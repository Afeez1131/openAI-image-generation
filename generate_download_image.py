import os
import requests
import urllib.request
import random

url = 'https://api.openai.com/v1/images/generations'
headers = {"Content-Type": "application/json",
           "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"}
data = {
    "prompt": "A pencil drawing of deadpool",
    "size": '256x256',
    "n": 3}

response = requests.post(url, json=data, headers=headers)
res = response.json()["data"]  # [0]["url"]
urls = [res[x]["url"] for x in range(len(res))]


def download_image(url_list: list):
    """this method will loop through the url_list,
    a list,containing URLS
    download the image from the URL, and save it locally"""
    for url in url_list:
        name = random.randrange(1, 100)
        full_name = str(name) + '.png'
        urllib.request.urlretrieve(url, full_name)
        print(f'image {full_name} download successfully...')


download_image(urls)
