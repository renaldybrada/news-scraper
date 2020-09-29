import re
import string

class NewsFormatService:
    def formatNews(self, content):
        result = content.replace('\n', '').replace('\"',"'").replace('\r','')
        return result

    def sanitize_text(self, text):        
        # parse text to lowercase
        text = text.lower()
        # remove text inside bracket
        text = re.sub('\[.*?\]', '', text)
        # sub \r with space
        text = re.sub('\r', ' ', text)
        # sub \n with space
        text = re.sub('\n', ' ', text)
        # sub punctuation with space
        text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
        # remove alphanumeric
        text = re.sub('\w*\d\w*', '', text)
        # sub multiple space to single space
        text = re.sub(' +', ' ', text)
        return text