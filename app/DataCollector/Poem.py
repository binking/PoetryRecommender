# Poem model

class Poem():
    def __init__(self, title, author, text):
        self.title = title
        self.author = author
        self.text = text
        self.click = 0
        #self.wordCount = self.parseText()

    def __repr__(self):
        return self.text

    def addClick(self):
        self.click += 1