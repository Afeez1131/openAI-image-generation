import random
import urllib.request
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
res = openai.Image.create_variation(
    image=open("838.png", "rb"),  # kindly replace "838.png" with an image on your local computer
    n=2,  # no of variations to generate
    size="1024x1024",
    response_format="url"
)

resp = res["data"]
resp_list = [resp[x]["url"] for x in range(len(resp))]  # list of all generated image variations


def download_image(url_list: list):
    """
    this method will loop through the url_list,
    a list,containing URLS
    download the image from the URL, and save it locally
    :param url_list:
    """
    for url in url_list:
        name = random.randrange(1, 100)
        full_name = str(name) + '-variations.png'
        urllib.request.urlretrieve(url, full_name)
        print(f'image {full_name} download succssfully...')


download_image(resp_list)
