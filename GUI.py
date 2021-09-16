#import sentencegenerator as sg
import random
from tkinter import *
import filehandler as fh
class Gui(Frame):

    def __init__(self, base = None):
        Frame.__init__(self, base)
        
        self.base = base
        self.init_gui()
        

    '''def generatePoem(self):
        
        sentencegen = sg.SentenceGenerator(random.randrange(4,24), self.txtPoem.get('1.0', 'end-1c'))
        sentences = sentencegen.generateSentences()
        self.poem = self.txtPoem.get("1.0", 'end-1c') + "\n \n"
        for sentence in sentences:
            self.poem += sentence + "\n"'''

    def sayHello(self):
        print(self.txtPoem.get('1.0', 'end-1c'))

    def init_gui(self):
        self.poem = "Hello"
        self.base.title('Poetry Agent')
        self.base.resizable()

        self.lblPad = Label(self.base)
        self.lblPad.pack(pady = 20)
        self.lblPoem = Label(self.base, text = "Enter a word or phrase based on the type of poem you'd like")
        self.lblPoem.pack(pady = 2)

        self.txtPoem = Text(self.base, height = 1, width = 40)
        self.txtPoem.pack(pady = 10)

        self.btnGeneratePoem = Button(self.base, text = "Generate Poem",command = lambda : self.sayHello(), height = 2, width = 15)
        self.btnGeneratePoem.pack(pady = 20)

        self.lblDisplay = Label(text = self.poem, height = 20, width = 40)
        self.lblDisplay.pack()


    def SaveToFile(self,name, poem):
        savetocorpus = fh.FileHandling("corpus.txt")
        savetocorpus.saveToFile(poem)
        poetry = fh.FileHandling(name)
        poetry.saveToFile(poem)



    

#Don't allow resizing in the x or y direction

#Don't allow the widgets inside to determine the frame's width / height

    
base = Tk() 
base.geometry("400x550") #You want the size of the app to be 500x500
app = Gui(base)
base.mainloop()
        