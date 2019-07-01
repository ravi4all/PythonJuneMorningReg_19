import json
import urllib.request as url

data = json.load(url.urlopen('https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=695e07af402f4b119f0703e9b19f4683'))
articles = data['articles']

for i in range(len(articles)):
    title = articles[i]['title']
    print(title)
    url.urlretrieve(articles[i]["urlToImage"], 'img_{}.jpg'.format(i))
