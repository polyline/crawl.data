# We are going to test how to crawl posts either on a public group or private group

import requests
from read_token import read_token


PUBLIC_GROUP_ID = "706068826168496"
PRIVATE_GROUP_ID = "1421863728080374"
ACCESS_TOKEN = read_token("token.json")

BASE_URL = 'https://graph.facebook.com/'
para_page = PUBLIC_GROUP_ID + "/feed"
para_token = "access_token=" + ACCESS_TOKEN

URL_PUBLIC = BASE_URL + para_page + '?' + para_token

# Verify the url
print("public", URL_PUBLIC)

# Verify Response
res = requests.get(URL_PUBLIC)
print("public", res)


BASE_URL = 'https://graph.facebook.com/'
para_page = PRIVATE_GROUP_ID + "/feed"
para_token = "access_token=" + ACCESS_TOKEN

URL_PRIVATE = BASE_URL + para_page + '?' + para_token

# Verify the url
print("private", URL_PRIVATE)

# Verify Response
res = requests.get(URL_PRIVATE)
print("private", res)
