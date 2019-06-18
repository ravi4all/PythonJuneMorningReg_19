import bs4
import urllib.request as url

path = 'https://www.flipkart.com/mi-led-smart-tv-4a-pro-80-cm-32-android/p/itmfdwh5jyqhmvzg?pid=TVSFDWH5K9N2FDTK&srno=s_1_1&otracker=search&otracker1=search&lid=LSTTVSFDWH5K9N2FDTK9CAPYS&fm=SEARCH&iid=426f7420-0b26-4a45-8eb6-c357841d1fa4.TVSFDWH5K9N2FDTK.SEARCH&ppt=sp&ppn=sp&ssid=xjtgzoyu2o0000001560829781339&qH=ebb7f8e6076c3747'
httpResponse = url.urlopen(path)

page = bs4.BeautifulSoup(httpResponse, 'lxml')

title = page.find('span', class_='_35KyD6')
print(title.text)

price = page.find('div',class_='_1vC4OE')
print(price.text)

highlights = page.find_all('li', class_='_2-riNZ')
for item in highlights:
    print(item.text)

productDesc = page.find('div', class_='_3la3Fn')
print(productDesc.text)

# rating = page.find_all('div', class_='hGSR34')
# review = page.find_all('p', class_='_2xg6Ul')
#
# for i,j in zip(rating, review):
#     print("Rating : {}, Review : {}".format(i.text, j.text))

div = page.find('div', class_='_39LH-M')
a_tag = div.find_all('a')
# print(a_tag[-1]['href'])
reviewsHref = a_tag[-1]['href']
newUrl = 'https://www.flipkart.com' + reviewsHref
# print(newUrl)

httpResponse = url.urlopen(newUrl)
page = bs4.BeautifulSoup(httpResponse, 'lxml')

rating = page.find_all('div', class_='hGSR34')
review = page.find_all('p', class_='_2xg6Ul')

for i,j in zip(rating, review):
    print("Rating : {}, Review : {}".format(i.text, j.text))