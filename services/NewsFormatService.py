class NewsFormatService:
    def formatNews(self, content):
        result = content.replace('\n', '').replace('\"',"'").replace('\r','')
        return result