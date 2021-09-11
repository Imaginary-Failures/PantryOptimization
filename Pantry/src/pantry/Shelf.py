class Shelf:
    
    def __init__(self, w, h):
            self.width = w,
            self.height = h,
            self.stacks = []
        
    pass

    def createStack(self):
        self.stacks.append(Stack()) #I need to have Stack constructor for this to work right now.
    pass

    def removeStack(self, index):
        self.stacks.remove(index)
    pass
    
    def getStack(self, index):
        return self.stacks[index]
    pass

    def searchFor(self, foodstuff):
        for(stack in self.stacks):
            if(stack.inStack(foodstuff)):
                return stack
        return None
    pass

    def getFoodstacks(self):
        return self.stacks
    pass

    def getWidth(self):
        return self.width
    pass

    def getHeight(self):
        return self.height
    pass

    def isEmpty(self):
        return self.stacks == []
    pass

    def __str__(self):
        return '' + str(self.width) + ', ' + str(self.height)
    def __repr__(self):
        return '' + str(self.width) + ', ' + str(self.height)
    