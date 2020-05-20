from .onlineNews import onlineNews

class CNN(onlineNews):
    def getIndex(self):
        soup = self.soupHTMLParser('https://www.cnnindonesia.com/')
        news_container = soup.select_one(".berita_terbaru_lst").select("article")

        # return news_container[1].select_one('.title').text
        news_index = []
        for new in news_container:
            if new.select_one('.title') != None:
                temp = {
                    'media': 'CNN',
                    'channel': 'cnn',
                    'title': new.select_one('.title').text,
                    'image': new.img['src'],
                    'link': new.a['href']
                }
                news_index.append(temp)
            
        return news_index

    def showNews(self, link):
        try:
            soup = self.soupHTMLParser(link)
        except:
            raise Exception("Something went wrong. check is your link valid") 
        
        paragraphs = soup.select_one("#detikdetailtext")
        if paragraphs != None :
            [junk.extract() for junk in paragraphs.select("script")]
            [junk.extract() for junk in paragraphs.select(".lihatjg")]
            [junk.extract() for junk in paragraphs.select(".linksisip")]
            paragraphs = paragraphs.text
        else:
            paragraphs = ''

        result = {
            'title': soup.title.string,
            'image': soup.find("meta", {"property":"og:image"})['content'],
            'content': paragraphs,
            'author': soup.find("meta", {"property":"article:author"})['content'],
            'editor': '',
            'date': soup.find("meta", {"name":"dtk:publishdate"})['content']
        }

        return result
        