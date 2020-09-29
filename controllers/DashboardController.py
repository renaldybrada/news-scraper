from controllers.BaseNewsController import BaseNewsController
from services.analytics.WordCountService import WordCountService
import random
from flask import url_for, request

class DashboardController(BaseNewsController):
    channels = ['kompas', 'detik', 'bbc', 'cnn', 'cnbc', 'idntimes', 'tribun']
    headlineByMedia = {}
    wordService = WordCountService()

    def showDashboard(self):
        # fetch headlines
        self.fetchAllHeadlines()

        analytics = self.wordService \
                        .createCorpus(self.headlineByMedia) \
                        .removeStopWord() \
                        .splitWords() \
                        .mostCommonWordsByMedia()

        return self.response.successResponse(
            {
                "headlines": {
                    "by_media": self.headlineByMedia,
                    "summary": self.headlineSummary()
                },
                "common_words": {
                    "by_media": analytics.commonWordByMedia
                }
            }    
        )

    def fetchAllHeadlines(self):
        for channel in self.channels:
            self.setChannel(channel)
            headlineTemp = self.channelObj.getIndex()

            # group headline by media 
            self.headlineByMedia[channel] = headlineTemp

    def headlineSummary(self):
        headlinePerMedia = 2

        result = []
        for channel, headlines in self.headlineByMedia.items():
            for x in range(headlinePerMedia):
                result.append(headlines[x])

        return result
