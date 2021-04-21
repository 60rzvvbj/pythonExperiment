import requests
import os
import bs4
path = 'resources/pic/'
if not os.path.exists(path):
    os.mkdir(path)
url = 'http://www.99118.com/'
res = requests.get(url)
res.encoding = 'gb2312'
for img in bs4.BeautifulSoup(res.text, 'lxml').findAll('img', class_="cImage8"):
    src = img['src']
    open(path + src.split('/')[-1], 'wb').write(requests.get(src).content)
