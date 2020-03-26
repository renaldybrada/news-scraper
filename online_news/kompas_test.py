import unittest
from kompas import Kompas

class TestKompas(unittest.TestCase):
    media = Kompas()
    mediaIdx = media.getIndex()

    def test_index(self):
        self.assertNotEqual(len(self.mediaIdx), 0)
    
    def test_news(self):
        for news in self.mediaIdx:
            content = self.media.showNews(news['link'])
            self.assertIsNotNone(content)