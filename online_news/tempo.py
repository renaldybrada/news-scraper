from .onlineNews import onlineNews

class Tempo(onlineNews):
    def getIndex(self):
        soup = self.soupHTMLParser('https://www.tempo.co/indeks')
        news_container = soup.select_one(".list-type-1").select(".card-type-1")

        news_index = []
        for news in news_container:
            imageUrl = news.select_one("a").img['src']
            betterImage = self.indexImage(imageUrl)

            temp = {
                'media': 'Tempo',
                'channel': 'tempo',
                'title': news.select_one(".title").get_text(),
                'image': betterImage,
                'link': news.select_one("a")['href']
            }
            news_index.append(temp)
            
        return news_index

    def showNews(self, link):
        try:
            soup = self.soupHTMLParser(link)
        except:
            raise Exception("Something went wrong. check is your link valid") 
        
        paragraphs = soup.select_one("#isi").select("p")
        content = ''

        for p in paragraphs:
            text = p.get_text()
            if "Baca juga" not in text:            
                content += text + " "  

        result = {
            'title': soup.title.string,
            'content': content,
            'image': soup.find("meta", {"property":"og:image"})['content'],
            'author': soup.find("meta", {"name":"author"})['content'],
            'editor': '',
            'date': ''
        }

        return result

    def indexImage(self, imageUrl):
        splitUrl = imageUrl.split("/")
        splitLast = splitUrl[8].split("_")
        splitLast[1] = "720.jpg"
        splitUrl[8] = "_".join(splitLast)

        joinUrl = "/".join(splitUrl)

        return joinUrl