import bs4
import urllib.request as url

path = 'https://www.flipkart.com/apple-iphone-8-plus-space-grey-64-gb/p/itmexrgvehtzhh9v?pid=MOBEXRGVQKBREZP8&srno=b_1_1&otracker=clp_banner_1_7.bannerX3.BANNER_apple-products-store_W8OZI07LNL&lid=LSTMOBEXRGVQKBREZP8VWK6HB&fm=neo%2Fmerchandising&iid=ebeccddc-aa08-41a3-b20f-3d012277144d.MOBEXRGVQKBREZP8.SEARCH&ppt=browse&ppn=browse&ssid=0bnyd84pts0000001560833490662'
httpResponse = url.urlopen(path)

page = bs4.BeautifulSoup(httpResponse, 'lxml')

div = page.find('div', class_='_39LH-M')
a_tag = div.find_all('a')
# print(a_tag[-1]['href'])
reviewsHref = a_tag[-1]['href']

for i in range(10):
    newUrl = 'https://www.flipkart.com' + reviewsHref + '&page={}'.format(i+1)

    httpResponse = url.urlopen(newUrl)
    page = bs4.BeautifulSoup(httpResponse, 'lxml')

    rating = page.find_all('div', class_='hGSR34')
    review = page.find_all('p', class_='_2xg6Ul')

    for i,j in zip(rating, review):
        print("Rating : {}, Review : {}".format(i.text, j.text))