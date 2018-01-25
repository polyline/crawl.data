import requests
from bs4 import BeautifulSoup
import json
from json import JSONDecodeError
import re
from pprint import pprint
import time
from browser import Browser

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
    
    tag = "jojoxdaily"
    
    quote_page = "https://www.instagram.com/%s/"%tag
    
    browser = Browser()
    
    browser.get(quote_page)
    signin_x_btn = browser.find_one('._5gt5u')
    if signin_x_btn:
        signin_x_btn.click()

    signin_x_btn = browser.find_one('._lilm5')
    if signin_x_btn:
        browser.scroll_down()
        browser.js_click(signin_x_btn)

    more_btn = browser.find_one('._1cr2e._epyes')
    
    more_btn.click()

    ele_posts = []

    while len(ele_posts) < 50:
        browser.scroll_down()
        #ele_posts = browser.find('._cmdpi ._mck9w')
    pageSource = browser.driver.page_source
    #print(len(ele_posts))
    #f.write("%s"%pageSource)
    
    response = BeautifulSoup(pageSource, "html.parser")
    #f.write("%s"%response)
    shared_data = extract_shared_data(response)
    user_profile = get_profile_information(shared_data)
    pprint(vars(user_profile))
    #f.write("%s"%shared_data)
    
    
    rows = response.find_all('div', '_70iju')
    links = []
    for row in rows:
        posts = row.find_all('a')
        for pt in posts:
            links.append(pt.attrs['href'])
    
    f.write("%s"%links)
    print(len(links))
    #response = BeautifulSoup(requests.get(quote_page).text, "html.parser")
    