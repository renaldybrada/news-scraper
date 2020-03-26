import requests
from bs4 import BeautifulSoup

class BBC:
    def soupHTMLParser(self, link):
        page = requests.get(link)
        HTMLcontent = page.content
        soup = BeautifulSoup(HTMLcontent, 'html.parser')

        return soup

    def getIndex(self):
        soup = self.soupHTMLParser('https://www.bbc.com/indonesia/topics/cjgn7k8yx4gt')
        news_container = soup.select_one(".lx-stream__feed").select(".lx-stream__post-container")

        # print(news_container)
        news_index = []
        for news in news_container:
            temp = {
                'media': 'BBC',
                'title': news.select_one(".lx-stream-post__header-text").get_text(),
                'image': news.select_one(".lx-stream-related-story--index-image-wrapper > img")['src'],
                'link': 'https://www.bbc.com' + news.select_one(".lx-stream-post__header-link")['href']
            }
            news_index.append(temp)
            
        return news_index

    def showNews(self, link):
        soup = self.soupHTMLParser(link)

        paragraphs = soup.select_one(".story-body__inner").find_all("p")

        content = ''
        author = ''

        for p in paragraphs:
            text = p.get_text()
            content += text + " " 

        if soup.select_one(".byline__name") != None:
            author = soup.select_one(".byline__name").string

        result = {
            'title': soup.title.string,
            'content': content,
            'author': author,
            'editor': '',
            'date': ''
        }

        return result