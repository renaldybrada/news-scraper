from .onlineNews import onlineNews

class IDNTimes(onlineNews):
    def getIndex(self):
        soup = self.soupHTMLParser('https://www.idntimes.com/news')
        news_container = soup.select_one("#latest-article").select(".box-latest > a")

        # print(news_container)
        news_index = []
        for new in news_container:
            temp = {
                'media': 'IDNTimes',
                'channel': 'idntimes',
                'title': new.img['alt'],
                'image': new.img['src'],
                'link': new['href']
            }
            news_index.append(temp)
            
        return news_index

    def showNews(self, link):
        try:
            soup = self.soupHTMLParser(link)
        except:
            raise Exception("Something went wrong. check is your link valid") 
        
        paragraphs = soup.select_one("#article-content").select("p")
        content = ''

        for p in paragraphs:
            text = p.get_text()
            if "Baca juga" not in text:            
                content += text + " " 

        result = {
            'title': soup.title.string,
            'image': soup.find("meta", {"property":"og:image"})['content'],
            'content': content,
            'author': soup.find_all("meta", {"name":"author"})[1]['content'],
            'editor': "",
            'date': ""
        }

        return result
        