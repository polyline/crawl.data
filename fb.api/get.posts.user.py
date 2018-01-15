import requests
from read_token import read_token

USER_ID = "337007633116"
ACCESS_TOKEN = read_token("token.json")

BASE_URL = 'https://graph.facebook.com/'
para_page = USER_ID + "/posts"
para_token = "access_token=" + ACCESS_TOKEN

URL = BASE_URL + para_page + '?' + para_token

# Verify the url
print(URL)

# Verify Response
res = requests.get(URL)
print(res)
