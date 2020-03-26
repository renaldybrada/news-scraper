import requests
from bs4 import BeautifulSoup
import json

class Tirto:
    def soupHTMLParser(self, link):
        page = requests.get(link)
        HTMLcontent = page.content
        soup = BeautifulSoup(HTMLcontent, 'html.parser')

        return soup

    def getIndex(self):
        soup = self.soupHTMLParser('https://tirto.id/q/current-issue-hPZ')
        news_container = soup.select_one(".my-5").select(".news-list-fade")

        news_index = [
            {
                'media': 'Tirto',
                'title': soup.select_one(".image-title").get_text(),
                'image': '',
                'link' : 'https://tirto.id' + soup.select_one(".z-2 > a")['href']
            }
        ]
        for news in news_container:
            temp = {
                'media': 'Tirto',
                'title': news.select_one(".list-title-outside-box").get_text(),
                'image': '',
                'link': 'https://tirto.id' + news.select_one(".m-0 > a")['href']
            }
            news_index.append(temp)
            
        return news_index

    def showNews(self, link):
        soup = self.soupHTMLParser(link)

        paragraphs = soup.select(".content-text-editor")[1].get_text()
        # print(paragraphs) 

        result = {
            'title': soup.title.string,
            'content': paragraphs,
            'author': soup.find("meta", {"name":"author"})['content'],
            'editor': '',
            'date': ''
        }

        return result