import Pantry, Shelf

class PantryTest:
    
    #test init
    print("Testing init Pantry with no args.")
    inputPantry = Pantry.Pantry();
    print("Testing init Pantry with specified 0 shelves.")
    testThisPantry = Pantry.Pantry(0);
    
    #test addShelf
    print("Testing addShelf() with no args.")
    inputPantry.addShelf();
    testThisPantry.addShelf(10, 15);
    testValue = "[{Width: 10; Height: 15}]"
    if(str(testThisPantry) != testValue) :
        print("Expected " + testValue + ", returned " + str(testThisPantry))
    else :
        print("AddShelf success")
        
    #test getShelves
    testThisPantry.addShelf(11, 16)
    testValue = "[{Width: 10; Height: 15}, {Width: 11; Height: 16}]"
    if(str(testThisPantry) != testValue) :
        print("Expected " + testValue + ", returned " + str(testThisPantry))
    else :
        print("getShelves success")
        
    #test getNumShelves
    testValue = 2
    if(testThisPantry.getNumShelves() != testValue) :
        print("Expected " + str(testValue) + ", returned " + str(testThisPantry.getNumShelves()))
    else :
        print("getNumShelves success")
        
    #test displayShelf():
    testValue = "{Width: 10; Height: 15}"
    if(str(testThisPantry.displayShelf(0)) != testValue) :
        print("Expected " + testValue + ", returned " + str(testThisPantry.displayShelf(0)))
    else :
        print("displayShelf at 0 success")
    testValue = "{Width: 11; Height: 16}"
    if(str(testThisPantry.displayShelf(1)) != testValue) :
        print("Expected " + testValue + ", returned " + str(testThisPantry.displayShelf(0)))
    else :
        print("displayShelf at 1 success")
    
    
