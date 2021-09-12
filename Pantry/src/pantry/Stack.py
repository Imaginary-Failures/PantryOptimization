
# import Foodstuff
#
# class Stack:
#     def __init__(self):
#         self.width = 0
#         self.height = 0
#         self.items = []
#
#     def addItem(self,item):
#         if not len(self.items):
#             self.width = item.width
# =======

import Foodstuff

class Stack:
    def __init__(self ):
        self.width = 0
        self.height = 0
        self.items = []
        self.stackable = True


    def addItem(self,item,stackable = True):
        if not len(self.items):
            self.width = item.depth
        if not stackable:
            self.stackable = False

        self.height += item.height
        self.items.append(item)

    def removeItem(self,item=0):
        "if no input. top item is removed. assume that item is in the stack"
        #need to modify = operator so the items are compared correctly

        if item: #if item is provided in args
            if(item.name == self.items[0].name) : #if item is the bottom of the stack
                removed = self.items[0]
                self.items.remove(removed)
                self.height -= removed.height
                if not self.isEmpty(): #modify width to next item on bottom if not empty
                    self.width = self.items[0].width
                else:
                    self.width = 0 #otherwise width is 0
                return removed
            else: #if item is not the bottom
                for i in self.items: #traverse through items[]
                    if i.name == item.name: #check if name is the same
                        self.items.remove(i)
                        self.height -= i.height
                        return i
        else: #if no arg, remove top of list (last item added)
            item = self.items.pop()
            self.height -= item.height
            return item

    def getItems(self):
        out = ""
        for i in self.items:
            out += i.name + "\n"
        return out
    
    def isEmpty(self):
        return self.items == []
    
    def __str__(self):
        return 'Stack with width: {}, height: {}'.format(str(self.width), str(self.height))

    def __repr__(self):
        return 'Stack with width: {}, height: {}'.format(str(self.width), str(self.height))
# =======
#         if item:
#             for i in self.items:
#                 if i.name == item.name:
#                     self.items.remove(i)
#                     self.height -= i.height
#                     return i
#         else:
#             item =self.items.pop()
#             self.height -= item.height
#             return item
#
#
#
#     def __str__(self):
#         return 'This stack has width, height: ' + str(self.width) + ', ' + str(self.height)
#
#
#     def __repr__(self):
#         return 'This stack has width, height: ' + str(self.width) + ', ' + str(self.height)
#
