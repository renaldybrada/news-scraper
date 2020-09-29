from services.NewsFormatService import NewsFormatService
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Dictionary.ArrayDictionary import ArrayDictionary
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

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
        cv = CountVectorizer()

        corpusHeadline = []
        channel = []
        for c, headline in self.corpus.items():
            corpusHeadline.append(headline)
            channel.append(c)

        data_cv = cv.fit_transform(corpusHeadline)
        
        # create data frame from split words
        self.splitWords = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
        self.splitWords.index = channel

        return self

    def mostCommonWordsByMedia(self):
        # get 30 most common words each channel
        wordCount = 30
        data = self.splitWords.transpose()
        
        for c in data.columns:
            top = data[c].sort_values(ascending=False).head(wordCount)
            combineKeyword = zip(top.index, top.values)
            resultKeyword = []
            for keyword in combineKeyword:
                tempKeyword = {
                    'keyword': keyword[0],
                    'count': int(keyword[1])
                }
                resultKeyword.append(tempKeyword)

            self.commonWordByMedia[c] = resultKeyword
            
        return self