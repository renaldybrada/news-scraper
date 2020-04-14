from flask import Flask
from controllers.NewsController import NewsController
from flask import request

app = Flask(__name__)
news = NewsController()

@app.route('/')
def hello_world():
    return {
        'message': 'it works!'
    }

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