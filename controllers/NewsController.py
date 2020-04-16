from online_news.kompas import Kompas
from online_news.detik import Detik
from online_news.bbc import BBC
from online_news.tirto import Tirto
from online_news.cnbc import CNBC
from flask import url_for, request

class NewsController:
    channels = ['kompas', 'detik', 'bbc', 'tirto', 'cnbc']
    
    channelObj = None
    
    def successResponse(self, data):
        response = {
            'status': 'success',
            'code': 200,
            'data': data
        }
        return response, 200

    def errorResponse(self, message, code):
        response = {
            'status': 'error',
            'code': code,
            'message': message,
        }
        return response, code

    def setChannel(self, channel):
        if channel == "kompas":
            self.channelObj = Kompas()
        elif channel == "detik":
            self.channelObj = Detik()
        elif channel == "bbc":
            self.channelObj = BBC()
        elif channel == "tirto":
            self.channelObj = Tirto()
        elif channel == "cnbc":
            self.channelObj = CNBC()
    
    def showChannels(self):
        data = self.channels
        return self.successResponse(data)

    def showHeadline(self, channel):
        self.setChannel(channel)
        data = self.channelObj.getIndex()
        for headline in data:
            headline['news_url'] = request.host_url + url_for('show_news', channel=headline['channel'], link=headline['link'])
        return self.successResponse(data)

    def showNews(self, channel, news_url):
        if news_url == None or news_url == '':
            return self.errorResponse('link cannot be empty', 422)

        self.setChannel(channel)
        data = self.channelObj.showNews(news_url)
        data['formated_news'] = self.formatNews(data['content'])
        return self.successResponse(data)

    def formatNews(self, content):
        result = content.replace('\n', '').replace('\"',"'")
        return result