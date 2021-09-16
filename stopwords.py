import filehandler as file



class StopWords:
    def __init__(self):
        self.file = file.FileHandling("stopwords.txt")
        self.words = self.file.readFromFile()

    def getStopWords(self):
        return self.words

    def isStopWord(self, word):
        if (word in self.words == True):
            return True
        else:
            return False
