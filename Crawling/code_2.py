import bs4
import urllib.request as url

movieName = input("Enter movie name : ")
path = "https://www.imdb.com/find?ref_=nv_sr_fn&q="+movieName

http = url.urlopen(path)
page = bs4.BeautifulSoup(http,'lxml')

td = page.find('td',class_='result_text')
#print(td)
a_tag = td.find('a')
#print(a_tag)
href = a_tag['href']

newUrl = 'https://www.imdb.com' + href
http_2 = url.urlopen(newUrl)
page_2 = bs4.BeautifulSoup(http_2, 'lxml')

summary = page_2.find('div', class_='summary_text')
print(summary.text.strip())

