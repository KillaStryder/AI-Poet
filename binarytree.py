class Stack:

     def __init__(self):
         self.values = []

     def isEmpty(self):
        Empty = False
        if self.values == []:
            Empty = True
        return Empty

     def push(self, value):
         self.values.append(value)

     def pop(self):
         return self.values.pop()

     def peek(self):
         return self.values[len(self.values)-1]

     def size(self):
         return len(self.values)


class NodeTree: 

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
    def insert(self,value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = NodeTree(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = NodeTree(value)
                else:
                    self.right.insert(value)
        else:
             self.value = value

    def findval(self, value):
        if value < self.value:
            if self.left is None:
                return False
            return self.left.findval(value)
        elif value > self.value:
            if self.right is None:
                return False
            return self.right.findval(value)
        else:
            return True

    def displayTree(self):
        if self.left:
            self.left.displayTree()
            return self.value,
        if self.right:
            self.right.displayTree()
            