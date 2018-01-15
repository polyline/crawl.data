import requests
from read_token import read_token
from read_response import read_response

PAGE_ID = '100000596238833'
POST_ID = '1935577203138802'

# I store the access_token in a seperated file, plz change to your own token
ACCESSTOKEN = read_token("token.json")

url = 'https://graph.facebook.com/'

para_comments = PAGE_ID + '_' + POST_ID + "/" + "comments"
para_accesstoken = "access_token="+ACCESSTOKEN
parameters = para_comments + "?" + para_accesstoken

# Verify url 
url = url + parameters
print(url)

res = requests.get(url)

# Verify Response
print(res)

# Try to read the data
read_response(res)
