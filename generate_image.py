import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')  # get the environmental variable
response = openai.Image.create(
    prompt="A fan art image for deadpool",  # the description of the image i want generated
    n=1,    # no of images to be generated
    size='256x256')  # resolution of the image

res = response["data"]
urls = [res[x]["url"] for x in range(len(res))]
print('URL: ', urls)


# sample res
"""
URL:  ['https://oaidalleapiprodscus.blob.core.windows.net/private/org-9LGdDgtWNf9H3ahrXtMGxLeE/user-ZGMS19ezW8ZGryPVOaroIQkc/img-FYFnjLHZlWDZdT0Pm02522Zq.png?st=2023-02-02T10%3A26%3A45Z&se=2023-02-02T12%3A26%3A45Z&sp=r&sv=2021-08-06&sr=b&rscd=inl
ine&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-02-01T21%3A24%3A05Z&ske=2023-02-02T21%3A24%3A05Z&sks=b&skv=2021-08-06&sig=D8%2BwQfpKJoyKUM1IKw/G1asu3VR/teQqRWsuPJPO1t0%3D', 'https:
//oaidalleapiprodscus.blob.core.windows.net/private/org-9LGdDgtWNf9H3ahrXtMGxLeE/user-ZGMS19ezW8ZGryPVOaroIQkc/img-pfIXQPy3wWGoNNV1JFyI75m6.png?st=2023-02-02T10%3A26%3A45Z&se=2023-02-02T12%3A26%3A45Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image
/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-02-01T21%3A24%3A05Z&ske=2023-02-02T21%3A24%3A05Z&sks=b&skv=2021-08-06&sig=3wRDKD8oyljMH7CGgvXK5uEVZDjJndYoN5zllehxvac%3D']
"""
