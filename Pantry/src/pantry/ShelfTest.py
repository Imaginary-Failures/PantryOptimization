import Shelf, Stack

class ShelfTest:
    
    #test init
    #test str
    testThisShelf = Shelf.Shelf(10, 15)
    testValue = "{Width: 10; Height: 15}"
    if(str(testThisShelf) != testValue) :
        print("Expected " + testValue + ", returned " + str(testThisShelf))
    else :
        print("init Shelf success")
    
    #test createStack
    #test getFoodstacks
    testThisShelf.createStack()
    testValue = "[Stack with width, height: 0, 0]"
    if(str(testThisShelf.getFoodstacks()) != testValue) :
        print("Expected " + testValue + ", returned " + str(testThisShelf.getFoodstacks()))
    else :
        print("createStack success")
    
    stackItem0 = testThisShelf.getFoodstacks()[0]
    #test getStack
    if(stackItem0 is not testThisShelf.getStack(0)) :
        print("Expected " + stackItem0 + ", returned " + testThisShelf.getStack(0))
    else :
        print("getStack success")
    
    #test removeStack
    testThisShelf.removeStack(stackItem0)
    testValue = "[]"
    if(str(testThisShelf.getFoodstacks()) != testValue) :
        print("Expected " + testValue + ", returned " + str(testThisShelf.getFoodstacks()))
    else :
        print("removeStack success")

    #test getWidth
    if(testThisShelf.getWidth() != 10) :
        print("Expected " + str(10) + ", returned " + testThisShelf.getWidth())
    else :
        print("getWidth success")
        
    #test getHeight
    if(testThisShelf.getHeight() != 15) :
        print("Expected " + str(15) + ", returned " + testThisShelf.getHeight())
    else :
        print("getHeight success")
        
    #test isEmpty
    if(testThisShelf.isEmpty() != True) :
        print("Expected " + True + ", returned " + testThisShelf.isEmpty())
    else :
        print("isEmpty success at true")
    testThisShelf.createStack()
    if(testThisShelf.isEmpty() != False) :
        print("Expected " + False + ", returned " + testThisShelf.isEmpty())
    else :
        print("isEmpty success at false")
    
    
    