import Stack, Foodstuff

class TestFood:
    def __init__(self, w, h, n):
        self.width = w
        self.height = h
        self.name = "test food" + n
        
    def __str__(self):
        return self.name + " with width, height: " + str(self.width) + ", " + str(self.height) + "\n"
    def __repr__(self):
        return self.name + " with width, height: " + str(self.width) + ", " + str(self.height) + "\n"
    
class StackTest:
    
    #test init
    #test str
    testThisStack = Stack.Stack()
    testValue = "Stack with width, height: 0, 0"
    if(str(testThisStack) != testValue) :
        print("Expected " + testValue + ", returned " + str(testThisStack))
    else :
        print("init Shelf success")
    
    testFoods = [TestFood(3, 2, "0"), TestFood(3, 2, "1"), TestFood(3, 1, "2"), TestFood(2, 1, "3")]
    #test addItem
    testThisStack.addItem(testFoods[0])
    testValue = "Stack with width, height: 3, 2"
    if(str(testThisStack) != testValue) :
        print("Expected " + testValue + ", returned " + str(testThisStack))
    else :
        print("addItem success at 1 item")
    #update height with new item
    testThisStack.addItem(testFoods[1])
    testThisStack.addItem(testFoods[2])
    testThisStack.addItem(testFoods[3])
    testValue = "Stack with width, height: 3, 6"
    if(str(testThisStack) != testValue) :
        print("Expected " + testValue + ", returned " + str(testThisStack))
    else :
        print("addItem success at >1 item")
    
    #test removeItem
    #test removeItem with no input
    testValue = testFoods[0:4]
    for index in range(len(testValue)-1, -1, -1):
        removed = testThisStack.removeItem()
        if(removed is not testValue[index]):
            print("Expected " + str(testValue[index]) + ", returned " + str(removed))
    print("removeItem success at no input")
    testValue = "Stack with width, height: 3, 6"
    
    testThisStack.addItem(testFoods[0]) #(3, 2)
    testThisStack.addItem(testFoods[3]) #(2, 1)
    #test removeItem with input
    removed = testThisStack.removeItem(testFoods[0])
    if(removed is not testFoods[0]):
            print("Expected " + testFoods[0].name + ", returned " + str(removed))
    else:
        print("removeItem success at provided input, change of base")
    #test removeItem width and height update
    testValue = "Stack with width, height: 0, 0"
    testThisStack.removeItem(testFoods[3])
    if(str(testThisStack) != testValue) :
        print("Expected " + testValue + ", returned " + str(testThisStack))
    else :
        print("removeItem success at last item")
    