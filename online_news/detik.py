from .onlineNews import onlineNews

class Detik(onlineNews):
    def getIndex(self):
        soup = self.soupHTMLParser('https://news.detik.com/indeks')
        news_container = soup.select_one("#indeks-container").select(".list-content__item")

        # print(news_container)
        news_index = []
        for news in news_container:
            imageUrl = news.select_one(".media__image > a > span > img")['src']
            betterImage = self.indexImage(imageUrl)

            temp = {
                'media': 'Detikcom',
                'channel': 'detik',
                'title': news.select_one(".media__title > a").get_text(),
                'image': betterImage,
                'link': news.select_one(".media__title > a")['href']
            }
            news_index.append(temp)
            
        return news_index

    def showNews(self, link):
        try:
            soup = self.soupHTMLParser(link)
        except:
            raise Exception("Something went wrong. check is your link valid") 

        content = ''
        paragraphs = soup.select_one(".detail__body-text")
        if paragraphs != None:
            paragraphs = paragraphs.find_all(["p", "strong"])
            for p in paragraphs:
                text = p.get_text()
                if 'Baca juga' not in text:
                    content += text + " " 
        else:
            content = 'text content not found. Link : ' + link

        result = {
            'title': soup.title.string,
            'image': soup.select_one(".detail__media-image > img")['src'],
            'content': content,
            'author': soup.find("meta", {"name":"dtk:author"})['content'],
            'editor': '',
            'date': soup.find("meta", {"name":"dtk:publishdate"})['content']
        }

        return result

    def indexImage(self, imageUrl):
        splitUrl = imageUrl.split("?")
        splitUrl[1] = "w=800&q=100"
        joinUrl = "?".join(splitUrl)
        
        return joinUrl