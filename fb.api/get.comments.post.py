import requests
from read_token import read_token

PAGE_ID = '897883826894958'
POST_ID = '2005435279473135'

# I store the access_token in a seperated file, plz change to your own token
ACCESSTOKEN = read_token("token.json")

url = 'https://graph.facebook.com/'

para_comments = PAGE_ID + '_' + POST_ID + "/" + "comments"
para_accesstoken = "access_token="+ACCESSTOKEN
parameters = para_comments + "?" + para_accesstoken

# construct url 
url = url + parameters
print(url)

res = requests.get(url)

print(res)