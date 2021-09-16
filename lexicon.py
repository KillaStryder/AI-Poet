import corpus as corpora
import nltk
import filehandler as fh
class Lexicon:

    def __init__(self, text):

        self.corpora = corpora.Corpus(text)
        self.text = text.split(" ")
        self.file = fh.FileHandling("lexicon.txt")
        self.lexicon = self.file.readFromFile()
        self.words = []

    def getCurrentLexicon(self):
        # current lexicon used for the current poem
        # get lexicon from file
        word =  {'word': "", 'pos': "", 'freq': 0}
        lexi = {'word': "", 'pos': "", 'freq': 0}
        for l in self.lexicon:
            lexi["word"] = l.split(",")[0]
            lexi["pos"] = l.split(",")[1]
            lexi["freq"] = l.split(",")[2]
            for w in self.corpora.getWords():
                print(w)
                if(w in lexi.get("word") is True):
                    lexi["freq"] = lexi.get("freq") + 1
                    self.words.append(l)
                else: 
                    word["word"] = w
                    word["pos"] = nltk.pos_tag([w])[0][1]
                    word["freq"] = 0
                    self.file.saveToFile(word)
                    self.words.append(word)
        return self.words

    def getVerbs(self):
        vbFile = fh.FileHandling("verb.txt")
        verbs = vbFile.readFromFile()
        cl = self.getCurrentLexicon()
        for verb in verbs:
            for word in cl:
                tag = word["pos"]
                if "r/<VB.*>" in tag and verb["word"] not in word["word"]:
                    verbs.append(word)
                    vbFile.saveToFile(word)
        return verbs

    def getNouns(self):
        nnFile = fh.FileHandling("noun.txt")
        nouns = nnFile.readFromFile()
        cl = self.getCurrentLexicon()
        for noun in nouns:
            for word in cl:
                tag = word["pos"]
                if "NN" in tag and noun["word"] not in word["word"]:
                    nouns.append(word)
                    nnFile.saveToFile(word)
        return nouns
    
    def getAdjectives(self):
        adjFile = fh.FileHandling("adj.txt")
        adjs = adjFile.readFromFile()
        cl = self.getCurrentLexicon()
        for adj in adjs:
            for word in cl:
                tag = word["pos"]
                if "JJ" in tag and adj["word"] not in word["word"]:
                    adjs.append(word)
                    adjFile.saveToFile(word)
        return adjs
    
    def getAdverbs(self):
        advFile = fh.FileHandling("verb.txt")
        advs = advFile.readFromFile()
        cl = self.getCurrentLexicon()
        for adv in advs:
            for word in cl:
                tag = word["pos"]
                if "r/<VB.*>" in tag and adv["word"] not in word["word"]:
                    adv.append(word)
                    advFile.saveToFile(word)
        return advs

    def getConjections(self):
        conjunctions = []
        for word in self.getCurrentLexicon():
            tag = nltk.pos_tag(word)[0][1]
            if "CC" in tag:
                conjunctions.append(word)
        return conjunctions





lexi = Lexicon("love") 
print(lexi.getCurrentLexicon())

    
   
