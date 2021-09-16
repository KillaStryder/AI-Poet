import random
import lexicon as lexi
import sentence as sent
#from System.IO import Path, File, FileInfo, FileAttributes
class SentenceGenerator:
        def __init__(self, numsentences, text):
                self.numsentences =numsentences
                self.lexi = lexi.Lexicon(text)

        
        def generateSentences(self):
                sentence = []
                isentence = 1
                sentType = random.randint(1,3)
                while isentence <= self.numsentences:
                        if sentType == 1:
                                self.sent = sent.Sentence(self.lexi.getNouns()[random.randint(1,(len(self.lexi.getNouns()) - 1))] + " " + self.lexi.getVerbs()[random.randint(1, (len(self.lexi.getVerbs())) - 1)])
                                isentence += 1
                                sentence.append(self.sent.makeSentence)
                        elif sentType == 2:
                                self.sent = sent.Sentence(self.lexi.getNouns()[random.randint(1,(len(self.lexi.getNouns()) - 1))] + " " + self.lexi.getVerbs()[random.randint(1, (len(self.lexi.getVerbs())) - 1)] + " " + self.lexi.getAdjectives()[random.randint(1, (len(self.lexi.getAdjectives()) -1))])
                                isentence += 1
                                sentence.append(self.sent.makeSentence)
                        else: 
                                self.sent = sent.Sentence(self.lexi.getNouns()[random.randint(1,(len(self.lexi.getNouns()) - 1))] + " " + self.lexi.getVerbs()[random.randint(1, (len(self.lexi.getVerbs())) - 1)] + " " + self.lexi.getAdjectives()[random.randint(1, (len(self.lexi.getAdjectives()) -1))] + self.lexi.getConjections()[random.randint(1, (len(self.lexi.getVerbs())) - 1)] + " " + self.lexi.getAdverbs()[random.randint(1, (len(self.lexi.getAdjectives()) -1))])
                                isentence += 1
                                sentence.append(self.sent.makeSentence)   
                return sentence