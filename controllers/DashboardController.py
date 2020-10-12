from controllers.BaseNewsController import BaseNewsController
from services.analytics.WordCountService import WordCountService
import random
from flask import url_for, request

class DashboardController(BaseNewsController):
    allHeadline = []
    headlineByMedia = {}
    analytics = {}
    wordService = WordCountService()

    def showDashboard(self):
        # fetch headlines
        self.fetchAllHeadlines()
        #fetch analytics
        self.fetchAnalytics()

        return self.response.successResponse(
            {
                "headlines": {
                    "by_media": self.headlineByMedia,
                    "summary": self.headlineSummary()
                },
                "common_words": {
                    "by_media": self.analytics.commonWordByMedia
                }
            }    
        )

    def fetchAnalytics(self):
        self.analytics = self.wordService \
                            .createCorpus(self.headlineByMedia) \
                            .removeStopWord() \
                            .splitWords()

    def fetchAllHeadlines(self):
        for channel in self.channels:
            self.setChannel(channel)
            try:
                headlineTemp = self.channelObj.getIndex()
            except Exception as e:
                print('Error get headline : ' + channel)
                continue

            self.allHeadline = self.allHeadline + headlineTemp 
            # group headline by media 
            self.headlineByMedia[channel] = headlineTemp

    def headlineSummary(self):
        headlinePerMedia = 2

        result = []
        for channel, headlines in self.headlineByMedia.items():
            for x in range(headlinePerMedia):
                result.append(headlines[x])

        return result