import sys
import filehandler as fh
import stopwords as sw
import nltk
class Corpus:

    def __init__(self,text = "random"):
        self.stopwords = sw.StopWords()
        self.file = fh.FileHandling("corpus.txt")
        self.words =[]
        self.sentences = []
        if (text is not "random"):
            self.text = text.split(" ")
        else: 
            self.text = ""
        

    def getSent(self):
        sentences = self.file.readFromFile()
        if "random" in self.text:
           return sentences
        else:
            for t in self.text:
                for s in sentences:
                    if (t in s.lower()) and (self.stopwords.isStopWord(t) is not True):
                        self.sentences.append(s)
                        print("sentence = " + s)
                    else: return sentences
        return self.sentences
            

    def getWords(self):
        self.sentences = self.getSent()
        for sentence in self.sentences:
            sentence = sentence.lower()
            words = sentence.split()
            print(words)
            for word in words:
                if (words.count(word) > 1) and (word not in self.words):
                    self.words.append(word)
                elif (words.count(word) > 1) and (word in self.words):
                    continue
                elif word in self.words:
                    continue
                else:
                     self.words.append(word)
        return self.words

cp = Corpus("love")
print("words: " + str(cp.getWords()))
         
        
        
    