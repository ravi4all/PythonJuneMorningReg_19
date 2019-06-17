import bs4
import urllib.request as url

http = url.urlopen('https://www.imdb.com/')
page = bs4.BeautifulSoup(http)

'''
div = page.find('div',id='trending-list-rank-item-1')
print(div.text)
'''

div = page.find_all('div',class_='trending-list-rank-item')
for item in div:
    print(item.text.strip())
