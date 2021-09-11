class Shelf:
    
    def __init__(self, w, h):
        self.thisshelf = {
            "width": w,
            "height": h,
            "stacks": []
        }
        
    pass

    def createStack(self):
        self.thisshelf["stacks"].append(new Stack()) #I need to have Stack constructor for this to work right now.
    pass

    def removeStack(self, index):
        self.thisshelf["stacks"].remove(index)
    pass
    
    def getStack(self, index):
        return self.thisshelf["stacks"][index]
    pass

    def searchFor(self, foodstuff):
        for(stack in self.thisshelf["stacks"]):
            if(stack.inStack(foodstuff)):
                return stack
        return None
    pass

    def getFoodstacks(self):
        return self.thisshelf["stacks"]
    pass

    def getWidth(self):
        return self.thisshelf["width"]
    pass

    def getHeight(self):
        return self.thisshelf["height"]
    pass

    def isEmpty(self):
        return self.thisshelf["stacks"] == []
    pass

    def __str__(self):
        return '' + str(self.thisshelf["width"]) + ', ' + str(self.thisshelf["height"])
    def __repr__(self):
        return '' + str(self.thisshelf["width"]) + ', ' + str(self.thisshelf["height"])
    