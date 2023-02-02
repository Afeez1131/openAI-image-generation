import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')  # get the environmental variable
response = openai.Image.create(
    prompt="A fan art image for deadpool",  # the description of the image i want generated
    n=2,    # no of images to be generated
    size='256x256')  # resolution of the image

res = response["data"]
urls = [res[x]["url"] for x in range(len(res))]
print('URL: ', urls)
