from services.database.CreateTables import MigrateTable
from services.database.dto.Headline import Headline
from services.database.dto.Analytic import Analytic
from services.database.InsertTable import InsertTable
from controllers.DashboardController import DashboardController
from controllers.BaseNewsController import BaseNewsController
import sys

def migrateTable():
    migrateTable = MigrateTable()
    migrateTable.migrate()

def insertTable():
    baseNews = BaseNewsController()
    dashboardData = DashboardController()
    dashboardData.fetchAllHeadlines()
    dashboardData.fetchAnalytics()

    # prepare headline item
    headlineItems = []
    imageDetailChannels = ['idntimes'] # list of channel need to scrap image in detail for replacing image in index
    for headline in dashboardData.allHeadline:
        baseNews.setChannel(headline['channel'])
        news = {
            'author': '',
            'editor': '',
            'content': '',
            'date': '',
            'image': ''
        }
        try:
            news = baseNews.channelObj.showNews(headline['link'])
        except Exception as e:
            print('Error get news : ' + headline['link'])
            continue

        # replace image for listed channels
        if headline['channel'] in imageDetailChannels:
            headline['image'] = news['image']

        temp = Headline(headline['channel'], headline['link'], headline['title'], headline['image'], \
                        news['author'], news['editor'], baseNews.newsFormat.formatNews(news['content']), news['date'])
        headlineItems.append(temp)
        
    # prepare analytic item
    analytic = dashboardData.analytics
    analyticItem = Analytic(str(analytic.commonWordByMedia))

    # insert data
    insertH = InsertTable()
    insertH.headline(headlineItems)
    insertA = InsertTable()
    insertA.analytics(analyticItem)


menus = ["migrate", "insert"]

arg = sys.argv
if len(arg) < 2:
    print('argumen yang dibutuhkan : ' + '/'.join(menus))
else:
    choosenMenu = arg[1]
    if any( choosenMenu in m for m in menus) == False:
        print('argumen yang dibutuhkan : ' + '/'.join(menus))
    else:
        if choosenMenu == "migrate":
            migrateTable()
        else:
            insertTable()