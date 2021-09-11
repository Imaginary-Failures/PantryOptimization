
import Foodstuff

class Stack:
    def __init__(self, ):
        self.width = 0
        self.height = 0
        self.items = []


    def addItem(self,item):
        if not len(self.items):
            self.width = item.width
        self.height += item.height
        self.items.append(item)

    def removeItem(self,item=0):
        "if no input. top item is removed. assume that item is in the stack"
        #need to modify = operator so the items are compared correctly
        if item:
            for i in self.items:
                if i.name == item.name:
                    self.items.remove(i)
                    self.height -= i.height
                    return i
        else:
            item =self.items.pop()
            self.height -= item.height
            return item



    def __str__(self):
        return 'This stack has width, height: ' + str(self.width) + ', ' + str(self.height)


    def __repr__(self):
        return 'This stack has width, height: ' + str(self.width) + ', ' + str(self.height)
