from flask import Flask
from controllers.NewsController import NewsController
from controllers.DashboardController import DashboardController
from flask import request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

news = NewsController()
dashboard = DashboardController()

@app.route('/')
def hello_world():
    return {
        'message': 'it works!'
    }

@app.route('/dashboard')
def show_dashboard():
    return dashboard.showDashboard()
    

@app.route('/channels')
def show_list():
    return news.showChannels()

@app.route('/headline/<channel>')
def show_headlines(channel):
    return news.showHeadline(channel)

@app.route('/news/<channel>')
def show_news(channel):
    link = request.args.get('link')
    return news.showNews(channel, link)


if __name__ == "__main__":
    app.run()