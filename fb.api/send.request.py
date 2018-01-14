import requests
from read_token import read_token

group_id = '884365888307469'

# I store the access_token in a seperated file, plz change to your own token

token = read_token("token.json")

# res = requests.get('https://graph.facebook.com/v2.9/{}/feed?access_token={}'.format(group_id, token))

message="Hello!!J"

para_message = "message="+ "\"" + message + "\""
para_accesstoken = "access_token="+token

parameters = para_message + "&" + para_accesstoken
print('https://graph.facebook.com/me/feed?' + parameters)
res = requests.post('https://graph.facebook.com/me/feed?' + parameters)

print(res)