from .onlineNews import onlineNews

class CNBC(onlineNews):
    def getIndex(self):
        soup = self.soupHTMLParser('https://www.cnbcindonesia.com/news/indeks/3')
        news_container = soup.select_one('.list.media_rows.middle.thumb.terbaru.gtm_indeks_feed').select('li')
        
        news_index = []
        for news in news_container:
            temp = {
                'media': 'CNBC',
                'channel': 'cnbc',
                'title': news.select_one(".box_text > h2").get_text(),
                'image': news.select_one("img")['src'],
                'link': news.select_one("a")['href']
            }
            news_index.append(temp)

        return news_index

    def showNews(self, link):
        soup = self.soupHTMLParser(link)
        paragraphs = soup.select_one('.detail_text')
        if paragraphs.center != None:
            paragraphs.center.extract()
        if paragraphs.table != None:
            paragraphs.table.extract()

        content = paragraphs.get_text()

        result = {
            'title': soup.title.string,
            'image': soup.find("meta", {"property":"og:image"})['content'],
            'content': content,
            'author': soup.find("meta", {"name":"dtk:author"})['content'],
            'editor': '',
            'date': soup.find("meta", {"name":"dtk:publishdate"})['content']
        }

        return result