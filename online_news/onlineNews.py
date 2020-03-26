import requests
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod

class onlineNews(ABC):
    def soupHTMLParser(self, link):
        page = requests.get(link)
        HTMLContent = page.content
        soup = BeautifulSoup(HTMLContent, 'html.parser')

        return soup

    def getIndex(self):
        pass

    def showNews(self):
        pass