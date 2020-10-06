from datetime import datetime

class Headline:
    def __init__(self, channel, link, title, image, author, editor, content, publishDate):
        self.channelName = channel
        self.originalLink = link
        self.title = title
        self.image = image
        self.author = author
        self.editor = editor
        self.content = content
        self.publishDate = publishDate
        self.createdAt = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    def toTuple(self):
        return (self.channelName, self.originalLink, self.title, self.image, self.author, self.editor, self.content, self.publishDate, self.createdAt)