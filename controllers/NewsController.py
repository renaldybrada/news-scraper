from controllers.BaseNewsController import BaseNewsController
from flask import url_for, request

class NewsController(BaseNewsController):    
    def showChannels(self):
        data = self.channels
        return self.response.successResponse(data)

    def showHeadline(self, channel):
        self.setChannel(channel)
        if(self.channelObj == None):
            return self.response.errorResponse('channel not found!', 404)

        data = self.channelObj.getIndex()
        for headline in data:
            headline['news_url'] = request.host_url + url_for('show_news', channel=headline['channel'], link=headline['link'])
        return self.response.successResponse(data)

    def showNews(self, channel, news_url):
        if news_url == None or news_url == '':
            return self.response.errorResponse('link cannot be empty', 422)

        self.setChannel(channel)
        if(self.channelObj == None):
            return self.response.errorResponse('channel not found!', 404)

        try:
            data = self.channelObj.showNews(news_url)
        except Exception as e:
            return self.response.errorResponse(str(e), 500)

        data['formated_news'] = self.newsFormat.formatNews(data['content'])
        return self.response.successResponse(data)