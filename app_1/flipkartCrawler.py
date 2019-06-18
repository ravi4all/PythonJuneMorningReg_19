import bs4
import urllib.request as url

path = 'https://www.flipkart.com/search?q=tv+&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY&as-backfill=on'
httpResponse = url.urlopen(path)

page = bs4.BeautifulSoup(httpResponse, 'lxml')

# div = page.find('div', class_='_3wU53n')
# print(div.text)

divList = page.find_all('div', class_='_3wU53n')
# for item in divList:
#     print(item.text)

priceList = page.find_all('div', class_='_1vC4OE')
# for price in priceList:
#     print(price.text)

for item, price in zip(divList, priceList):
    print(item.text)
    print(price.text)
    print("-----------------------------")