from .onlineNews import onlineNews

class Kompas(onlineNews):
    def getIndex(self):
        soup = self.soupHTMLParser('https://indeks.kompas.com/')
        news_container = soup.select_one(".latest--indeks").select(".article__asset > a")

        # print(news_container)
        news_index = []
        for new in news_container:
            temp = {
                'media': 'Kompas',
                'title': new.img['alt'],
                'image': new.img['src'],
                'link': new['href']
            }
            news_index.append(temp)
            
        return news_index

    def showNews(self, link):
        soup = self.soupHTMLParser(link)
            
        paragraphs = soup.select_one(".read__content").select("p")
        content = ''

        for p in paragraphs:
            text = p.get_text()
            if "Baca juga" not in text:            
                content += text + " " 

        result = {
            'title': soup.title.string,
            'content': content,
            'author': soup.find("meta", {"name":"content_author"})['content'],
            'editor': soup.find("meta", {"name":"content_editor"})['content'],
            'date': soup.find("meta", {"name":"content_PublishedDate"})['content']
        }

        return result
        