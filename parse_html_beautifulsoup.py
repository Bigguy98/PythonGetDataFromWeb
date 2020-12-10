import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'https://www.dienmayxanh.com/'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # print(tag)
    # print('URL:', tag.get('href', None))
    # if tag.contents:
    #     print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)