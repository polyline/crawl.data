import requests
from read_token import read_token

# Get comments of a public video from a fan page

PAGE_ID = '13062516037'
VIDEO_ID = '10157061710976038'

# I store the access_token in a seperated file, plz change to your own token
ACCESSTOKEN = read_token("token.json")

BASE_URL = 'https://graph.facebook.com/'
para_comments = PAGE_ID + '_' + VIDEO_ID + "/comments"
para_token = "access_token=" + ACCESSTOKEN

URL = BASE_URL + para_comments + '?' + para_token

# Verify the URL
print(URL)

res = requests.get(URL)

# Verify the response
print(res)
