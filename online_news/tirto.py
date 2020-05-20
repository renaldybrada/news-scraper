from .onlineNews import onlineNews

class Tirto(onlineNews):
    def getIndex(self):
        soup = self.soupHTMLParser('https://tirto.id/q/current-issue-hPZ')
        news_container = soup.select_one(".my-5").select(".news-list-fade")

        news_index = [
            {
                'media': 'Tirto',
                'channel': 'tirto',
                'title': soup.select_one(".image-title").get_text(),
                'image': '',
                'link' : 'https://tirto.id' + soup.select_one(".z-2 > a")['href']
            }
        ]
        for news in news_container:
            temp = {
                'media': 'Tirto',
                'channel': 'tirto',
                'title': news.select_one(".list-title-outside-box").get_text(),
                'image': '',
                'link': 'https://tirto.id' + news.select_one(".m-0 > a")['href']
            }
            news_index.append(temp)
            
        return news_index

    def showNews(self, link):
        try:
            soup = self.soupHTMLParser(link)
        except:
            raise Exception("Something went wrong. check is your link valid") 
        
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