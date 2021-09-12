import Stack

class Shelf:
    
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.stacks = []
    pass

    def createStack(self):
        self.stacks.append(Stack()) 
        pass

    def removeStack(self, index):
        self.stacks.remove(index)
    pass
    
    def getStack(self, index):
        return self.stacks[index]
    pass

    def searchFor(self, foodstuff):
        for scannedStack in self.stacks :
            if(scannedStack.inStack(foodstuff)):
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
        return '{Width: ' + str(self.width) + '; Height: ' + str(self.height) + '}'
    def __repr__(self):
        return '{Width: ' + str(self.width) + '; Height: ' + str(self.height) + '}'
    
    #If self is referencing compared object, return true
    #If compared object is null, return false
    #If other is not a Shelf, return false
    #If the width and height of the Shelves are not the same, return false
    #Else the shelves are equal
    def equals(self, other):
        if(self is other):
            return True
        elif(other is None):
            return False
        elif(type(self) != type(other)):
            return False
        elif(str(self) != str(other)):
                return False                                      
        else:
                return True
        pass