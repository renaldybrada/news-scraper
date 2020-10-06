from services.database.CreateTables import MigrateTable
from services.database.dto.Headline import Headline
from services.database.dto.Analytic import Analytic
from services.database.InsertTable import InsertTable
from controllers.DashboardController import DashboardController
import sys

def migrateTable():
    migrateTable = MigrateTable()
    migrateTable.migrate()

def insertTable():
    dashboardData = DashboardController()
    dashboardData.fetchAllHeadlines()
    dashboardData.fetchAnalytics()

    # prepare headline item
    headlineItems = []
    for headline in dashboardData.allHeadline:
        temp = Headline(headline['channel'], headline['link'], headline['title'], headline['image'])
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