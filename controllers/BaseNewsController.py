from online_news.kompas import Kompas
from online_news.detik import Detik
from online_news.bbc import BBC
from online_news.cnn import CNN
from online_news.cnbc import CNBC
from online_news.idntimes import IDNTimes
from online_news.tribunnews import TribunNews
from online_news.tempo import Tempo
from services.NewsFormatService import NewsFormatService
from services.ResponseService import ResponseService

class BaseNewsController:
    newsFormat = NewsFormatService()
    response = ResponseService()
    channels = ['kompas', 'detik', 'bbc', 'cnn', 'cnbc', 'idntimes', 'tribun', 'tempo']
    channelObj = None

    def setChannel(self, channel):
        if channel == "kompas":
            self.channelObj = Kompas()
        elif channel == "detik":
            self.channelObj = Detik()
        elif channel == "bbc":
            self.channelObj = BBC()
        elif channel == "cnn":
            self.channelObj = CNN()
        elif channel == "cnbc":
            self.channelObj = CNBC()
        elif channel == "idntimes":
            self.channelObj = IDNTimes()
        elif channel == "tribun":
            self.channelObj = TribunNews()
        elif channel == "tempo":
            self.channelObj = Tempo()
        else:
            self.channelObj = None