from datetime import datetime

class Analytic:
    def __init__(self, content):
        self.content = content
        self.createdAt = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    def toTuple(self):
        return (self.content, self.createdAt)