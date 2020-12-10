import urllib.request
import re # regular expression

url = 'https://www.dienmayxanh.com/'
html = urllib.request.urlopen(url).read()
links = re.findall(b'href="(https://.*?)"', html)

for link in links:
    print(link.decode())