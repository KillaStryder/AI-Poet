class FileHandling:
    def __init__(self, filename):
        self.filename = filename

    def readFromFile(self):
        s = None
        try:
            f = open(self.filename, "r")
            s = f.readlines()
            f.close()
        except IOError:
            print("Cannot open the file")
        return s

    def saveToFile(self, text):
        try:
            f = open(self.filename, 'a')
            f.write(text)
            f.close()
        except FileNotFoundError:
            print("Cannot open the file")