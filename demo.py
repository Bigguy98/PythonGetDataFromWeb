import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
# url of source page
url = 'https://www.thegioididong.com/dtdd/'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# get all <img> elements
imgs = soup('img')
sources = []
for img in imgs:
    # get src of image
    src = img.get('src') if img.get('src') != None else (img.get('data-src') if img.get('data-src') != None else img.get('data-original'))
    # process src, remove ?......
   
    if '?' in src:
        src = src[:src.index('?')]
    sources.append(src if 'https:' in src else 'https:' + src)

for src in sources:
    print("Downloading image: " + src)
    # read image
    img = urllib.request.urlopen(src).read()
    # split to get image name
    imageName = src.split('/')[-1]
    # write image to folder
    fhand = open('images/' + imageName, 'wb')
    fhand.write(img)
    fhand.close()
    

