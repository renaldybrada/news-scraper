from online_news.kompas import Kompas
from online_news.detik import Detik
from online_news.bbc import BBC
from online_news.tirto import Tirto
from online_news.cnbc import CNBC

class Main:
    mediaObject = None
    medias = {
            "kompas": "Kompas",
            "detik": "Detik",
            "bbc": "BBC Indonesia",
            "tirto": "Tirto",
            "cnbc": "CNBC"
        }
    selectMedia = ''

    def initiate(self):
        self.showMediaMenu()

    def checkInput(self, keyword):
        exitKeywords = ["quit", "exit", "keluar"]
        menuKeywords = ["menu", "channel"]

        if keyword in exitKeywords:
            exit()
        elif keyword in menuKeywords:
            self.showMediaMenu()

    # Media menu
    def showMediaMenu(self):
        mediaExample = ''

        print("Media yang tersedia : ")
        for key, val in enumerate(self.medias):
            print("[" + str(key +1) + "] " + self.medias[val])
            if key < 5 :
                mediaExample += val + " / "

        selectMedia = input('mau baca berita dari media apa ? ('+ mediaExample +' exit) ') 
        print("")

        if selectMedia not in self.medias:
            if selectMedia in ["quit", "exit", "keluar"]:
                exit
            else:
                self.showMediaMenu()
        else:
            self.selectMedia = selectMedia
            self.showIndexByMedia()

    # Show Index by media
    def showIndexByMedia(self):
        if self.selectMedia == "kompas":
            self.mediaObject = Kompas()
        elif self.selectMedia == "detik":
            self.mediaObject = Detik()
        elif self.selectMedia == "bbc":
            self.mediaObject = BBC()
        elif self.selectMedia == "tirto":
            self.mediaObject = Tirto()
        elif self.selectMedia == "cnbc":
            self.mediaObject = CNBC()

        newsIndex = self.mediaObject.getIndex()
        
        print('indeks berita : ' + self.selectMedia)
        print("")
        for idx, news in enumerate(newsIndex):
            print("[" + str(idx + 1) + "] " + news['title'])
            print("")

        selectNewsIdx = input('pilih berita [1/2/3/..] ')
        print("")
        
        try:
            selectNewsIdx = int(selectNewsIdx) - 1
            if selectNewsIdx < 0:
                raise ValueError('news not found : negative index')
            self.showNews(newsIndex[selectNewsIdx]['link'])
        except:
            print('berita tidak tersedia !')
            print("")
            self.showIndexByMedia()

    def showNews(self, link):
        news = self.mediaObject.showNews(link)
        print(news['title'])
        print("")
        print(news['content'])
        print("")

        nextAction = input("Tekan 'enter' untuk kembali ke index berita " + self.selectMedia + " ,ketik 'menu' untuk kembali kembali memilih media ")
        print("")
        
        if nextAction == 'menu':
            self.showMediaMenu()
        else:
            self.showIndexByMedia()

main = Main()
main.initiate()