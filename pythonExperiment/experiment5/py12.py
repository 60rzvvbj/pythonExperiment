import requests
import bs4


def getChapter(name, url):
    file = open("resources/novel.txt", "a+", encoding="utf-8")
    file.write(name+"\n")
    for p in bs4.BeautifulSoup(requests.get(url=url).text, "lxml").find("div", class_="read-content j_readContent").findAll("p"):
        file.write(p.text+"\n")
        print(p.text)


url = "https://book.qidian.com/info/1018027842#Catalog"
resp = requests.get(url=url)
resp.encoding = "utf-8"
lst = bs4.BeautifulSoup(resp.text, "lxml").find("ul", class_="cf").findAll("a")
for item in lst[:10]:
    chapter = item.string
    url = item.get("href")
    getChapter(chapter, "https:" + url)
