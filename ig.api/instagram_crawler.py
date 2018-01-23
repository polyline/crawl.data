import urllib.request
from bs4 import BeautifulSoup

tag = "cal_foodie"

quote_page = "https://www.instagram.com/%s/"%tag
page = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
print(soup.prettify()[0:100])