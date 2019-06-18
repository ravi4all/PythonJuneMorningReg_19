import urllib.request as url

http = url.urlopen("https://www.marvel.com/movies")
print(http)

url.urlretrieve("https://terrigen-cdn-dev.marvel.com/content/prod/1x/avengersendgame_lob_crd_05_2.jpg","img_1.jpg")
