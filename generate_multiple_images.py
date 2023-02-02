import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')  # get the environmental variable
response = openai.Image.create(
	prompt="A fan art image for deadpool",
	n=2, size='256x256')
res = response["data"]
urls = [res[x]["url"] for x in range(len(res))]
print('URL: ', urls)



#sample result
"""
URL:  ['https://oaidalleapiprodscus.blob.core.windows.net/private/org-9LGdDgtWNf9H3ahrXtMGxLeE/user-ZGMS19ezW8ZGryPVOaroIQkc/img-bYidYQAd9EITYA2VPDbKMaqT.png?st=2023-02-02T10%3A31%3A58Z&se=2023-02-02T12%3A31%3A58Z&sp=r&sv=2021-08-06&sr=b&rscd=inl
ine&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-02-01T21%3A21%3A55Z&ske=2023-02-02T21%3A21%3A55Z&sks=b&skv=2021-08-06&sig=aDi4Q2WZeKF5/x%2BdzVhK56Bg1b2dlqRoSCIdwxJX2x4%3D', 'https:
//oaidalleapiprodscus.blob.core.windows.net/private/org-9LGdDgtWNf9H3ahrXtMGxLeE/user-ZGMS19ezW8ZGryPVOaroIQkc/img-gCBlWnnyjEU7IFbE4wBkqfia.png?st=2023-02-02T10%3A31%3A59Z&se=2023-02-02T12%3A31%3A59Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image
/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-02-01T21%3A21%3A55Z&ske=2023-02-02T21%3A21%3A55Z&sks=b&skv=2021-08-06&sig=L8EzZSoe%2BfsZzz/fVd/Z00q3w4iAIdJ79gOK1k/tDsg%3D']
"""
