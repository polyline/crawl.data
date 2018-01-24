import requests
from bs4 import BeautifulSoup
import json
from json import JSONDecodeError
import re
from pprint import pprint

filepath = "./output"
f = open(filepath, 'w', encoding="utf-8")

class InstagramUser:
    def __init__(self, user_id, username=None, bio=None, followers_count=None, following_count=None, is_private=False, user_picture=None):
        
        self.id = user_id
        self.username = username
        self.bio = bio
        self.followers_count = followers_count
        self.following_count = following_count
        self.is_private = is_private
        self.user_picture = user_picture

def extract_shared_data(doc):

    for script in doc.find_all("script"):
        if script.text.startswith("window._sharedData ="):
            shared_data = re.sub("^window\._sharedData = ", "", script.text)
            shared_data = re.sub(";$", "", shared_data)
            shared_data = json.loads(shared_data)
            shared_data = shared_data['entry_data']['ProfilePage'][0]['user']
            return shared_data

def get_profile_information(data):
    
    return InstagramUser(
        user_id = data['id'],
        username = data['full_name'],
        bio = data['biography'],
        followers_count = data['followed_by']['count'],
        following_count = data['follows']['count'],
        is_private = data['is_private'],
        user_picture = data['profile_pic_url']
    )

if __name__ == '__main__':
    
    tag = "cal_foodie"

    quote_page = "https://www.instagram.com/%s/"%tag
    response = BeautifulSoup(requests.get(quote_page).text, "html.parser")
    #print(response)
    #f.write("%s"%response)
    shared_data = extract_shared_data(response)
    user_profile = get_profile_information(shared_data)
    #f.write("%s"%shared_data)
    media = shared_data['media']['nodes']
    f.write("%s"%media)
    #pprint(vars(user_profile))