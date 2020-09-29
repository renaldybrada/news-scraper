from controllers.BaseNewsController import BaseNewsController
from flask import url_for, request

class DashboardController(BaseNewsController):
    channels = ['kompas', 'detik', 'bbc', 'cnn', 'cnbc', 'idntimes', 'tribun']
    headlinesPool = {}

    def showDashboard(self):
        # fetch headlines
        for channel in self.channels:
            self.setChannel(channel)
            headlineTemp = self.channelObj.getIndex()
            self.headlinesPool[channel] = headlineTemp
            
        return self.response.successResponse(self.headlinesPool)
