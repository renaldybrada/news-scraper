from datetime import datetime

class Headline:
    def __init__(self, channel, link, title, image):
        self.channelName = channel
        self.originalLink = link
        self.title = title
        self.image = image
        self.createdAt = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    def toTuple(self):
        return (self.channelName, self.originalLink, self.title, self.image, self.createdAt)