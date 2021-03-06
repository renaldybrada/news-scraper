from .onlineNews import onlineNews

class Kompas(onlineNews):
    def getIndex(self):
        soup = self.soupHTMLParser('https://indeks.kompas.com/')
        news_container = soup.select_one(".latest--indeks").select(".article__asset > a")

        # print(news_container)
        news_index = []
        for new in news_container:
            imageUrl = new.img['src']
            betterImage = self.indexImage(imageUrl)

            temp = {
                'media': 'Kompas',
                'channel': 'kompas',
                'title': new.img['alt'],
                'image': betterImage,
                'link': new['href']
            }
            news_index.append(temp)
            
        return news_index

    def showNews(self, link):
        try:
            soup = self.soupHTMLParser(link)
        except:
            raise Exception("Something went wrong. check is your link valid") 
        
        paragraphs = soup.select_one(".read__content").select("p")
        content = ''

        for p in paragraphs:
            text = p.get_text()
            if "Baca juga" not in text:            
                content += text + " " 

        result = {
            'title': soup.title.string,
            'image': soup.find("meta", {"property":"og:image"})['content'],
            'content': content,
            'author': soup.find("meta", {"name":"content_author"})['content'],
            'editor': soup.find("meta", {"name":"content_editor"})['content'],
            'date': soup.find("meta", {"name":"content_PublishedDate"})['content']
        }

        return result
        
    def indexImage(self, imageUrl):
        splitUrl = imageUrl.split("/")
        remove_index_point = 3

        for x in range(4):
            removeString = splitUrl.pop(remove_index_point)

        joinUrl = "/".join(splitUrl)

        return joinUrl