import requests
from read_token import read_token

# Get comments of a public video from a fan page

PAGE_ID = '13062516037'

# I store the access_token in a seperated file, plz change to your own token
ACCESSTOKEN = read_token("token.json")

BASE_URL = 'https://graph.facebook.com/'
para_page = PAGE_ID + "/posts"
para_token = "access_token=" + ACCESSTOKEN

URL = BASE_URL + para_page + '?' + para_token

# Verify the url
print(URL)

res = requests.get(URL)
