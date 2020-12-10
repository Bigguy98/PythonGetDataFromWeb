import urllib.request, urllib.parse, urllib.error


# url = 'https://cdn.tgdd.vn/Products/Images/1942/219259/TimerThumb/samsung-ua50tu8100-(9).jpg'
url = 'https://cdn0.fahasa.com/media/catalog/product/cache/1/small_image/400x400/9df78eab33525d08d6e5fb8d27136e95/n/a/naruto-tap-47.jpg'
img = urllib.request.urlopen(url).read()
imageName = url.split('/')[-1]
# process image name
if '?' in imageName:
    imageName = imageName[:imageName.index('?')]

fhand = open('images/' + imageName, 'wb')
fhand.write(img)
fhand.close()