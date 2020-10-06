from .onlineNews import onlineNews

class TribunNews(onlineNews):
    def getIndex(self):
        news_index = []
        
        soup = self.soupHTMLParser('https://www.tribunnews.com/news')
        news_container = soup.select_one("#latestul").select('.art-list > .pos_rel > a')

        for new in news_container:
            imageUrl = new.img['src']
            betterImage = self.indexImage(imageUrl)

            temp = {
                'media': 'Tribunnews',
                'channel': 'tribun',
                'title': new['title'],
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
        
        paragraphs = soup.select_one(".txt-article").select("p")
        content = ''

        for p in paragraphs:
            text = p.get_text()
            if "Baca: " not in text:
                if "Penulis : " not in text:
                    if "Artikel ini telah tayang " not in text:            
                        content += text + " " 

        result = {
            'title': soup.title.string,
            'image': soup.select_one(".imgfull")['src'],
            'content': content,
            'author': "",
            'editor': "",
            'date': ""
        }

        return result
    
    def indexImage(self, imageUrl):
        splitUrl = imageUrl.split("/")
        if (len(splitUrl) > 6):
            splitUrl[6] = "images"
            joinUrl = "/".join(splitUrl)
            
            return joinUrl
        else:
            return imageUrl