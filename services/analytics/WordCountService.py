from services.NewsFormatService import NewsFormatService
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Dictionary.ArrayDictionary import ArrayDictionary
from collections import Counter

class WordCountService:
    formatText = NewsFormatService()
    corpus = {}
    splitWords = None
    commonWordByMedia = {}

    def createCorpus(self, newsHeadline):
        for channel, headline in newsHeadline.items():
            newsTemp = ""
            for news in headline:
                newsTemp = newsTemp + news["title"] + " "
                self.corpus[channel] = self.formatText.sanitize_text(newsTemp)

        return self

    def removeStopWord(self):
        stopWordFactory = StopWordRemoverFactory()
        stopWord = stopWordFactory.create_stop_word_remover()

        for channel in self.corpus:
            text = self.corpus[channel]
            result = stopWord.remove(text)
            self.corpus[channel] = result

        return self

    def splitWords(self):
        corpusHeadline = []
        channel = []
        for c, headline in self.corpus.items():
            self.commonWordByMedia[c] = Counter(headline.split()).most_common(30)

        return self