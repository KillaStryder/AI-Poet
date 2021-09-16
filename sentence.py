from binarytree import Stack, NodeTree
import nltk


class Sentence:
    def __init__(self, text):
        self.text = text

    def makeSentence(self):
        wlist = self.text.split()
        wStack = Stack()
        eTree = NodeTree('')
        wStack.push(eTree)
        currentTree = eTree
        for i in wlist:
            if nltk.pos_tag([i])[0][1] == 'NN':
                currentTree.insert('')
                wStack.push(currentTree)
                currentTree = currentTree.left()
            elif i not in ['VB','VBZ', 'DT', 'JJ','RB', '']:
                currentTree.insert((str(i)))
                parent = wStack.pop()
                currentTree = parent
            elif i in ['NNP', 'NNS', 'NN']:
                currentTree.insert((i))
                currentTree.right('')
                wStack.push(currentTree)
                currentTree = currentTree.findval(currentTree.right)
            elif i == ')':
                currentTree = wStack.pop()
            else:
                raise ValueError
        return eTree.displayTree()

    
