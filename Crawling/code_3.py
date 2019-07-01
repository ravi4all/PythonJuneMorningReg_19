import bs4
import urllib.request as url
moviename=input("enter your movie name")
path="https://www.imdb.com/find?ref_=nv_sr_fn&q="+moviename
http=url.urlopen(path)
page=bs4.BeautifulSoup(http,"lxml")
rak=page.find('td',class_="result_text")
print(rak.text)
a_tag=rak.find('a')
href=a_tag['href']
newurl="https://www.imdb.com"+href
http_2=url.urlopen(newurl)
page_2=bs4.BeautifulSoup(http_2,"lxml")
tak=page_2.find('div',class_="summary_text")
print(tak.text.strip())
ton=page_2.find('div',class_="inline canwrap")
p=ton.find('p')
span=p.find("span")
print("Storyline")
print(span.text.strip())
raki=page_2.find('div',class_="user-comments")
a1=raki.find_all('a')
a2=a1[-1]
href_2=a2['href']
thirdurl="https://www.imdb.com"+href_2
http_3=url.urlopen(thirdurl)
page_3=bs4.BeautifulSoup(http_3,"lxml")
rating=page_3.find_all('span',class_="rating-other-user-rating")
#print(rating.text)
review=page_3.find_all('div',class_="text show-more__control")
#print(review.text)
