from .onlineNews import onlineNews

class BBC(onlineNews):
    def getIndex(self):
        soup = self.soupHTMLParser('https://www.bbc.com/indonesia/topics/cjgn7k8yx4gt')
        news_container = soup.select_one(".lx-stream__feed").select(".lx-stream__post-container")

        # print(news_container)
        news_index = []
        for news in news_container:
            imageUrl = news.select_one(".lx-stream-related-story--index-image-wrapper > img")['src']
            betterImage = self.indexImage(imageUrl)
            temp = {
                'media': 'BBC',
                'channel': 'bbc',
                'title': news.select_one(".lx-stream-post__header-text").get_text(),
                'image': betterImage,
                'link': 'https://www.bbc.com' + news.select_one(".lx-stream-post__header-link")['href']
            }
            news_index.append(temp)
            
        return news_index

    def showNews(self, link):
        try: 
            soup = self.soupHTMLParser(link)
        except:
            raise Exception("Something went wrong. check is your link valid") 
        
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
            'image': soup.find("meta", {"property":"og:image"})['content'],
            'content': content,
            'author': author,
            'editor': '',
            'date': ''
        }

        return result

    def indexImage(self, imageUrl):
        splitUrl = imageUrl.split("/")
        splitUrl[5] = "800" # 800 pixel width
        joinUrl = "/".join(splitUrl)
        
        return joinUrl