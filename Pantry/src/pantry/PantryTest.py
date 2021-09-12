import Pantry, Shelf

class PantryTest():
    
    #test init
    print("Testing init Pantry with no args.")
    inputPantry = Pantry.Pantry();
    print("Testing init Pantry with specified 0 shelves.")
    emptyPantry = Pantry.Pantry(0);
    
    #test addShelf
    print("Testing addShelf() with no args.")
    inputPantry.addShelf();
    emptyPantry.addShelf(10, 15);
    testValue = "[{Width: 10; Height: 15}]"
    if(str(emptyPantry) != testValue) :
        print("Expected " + testValue + ", returned " + str(emptyPantry))
    else :
        print("AddShelf success")
        
    #test getShelves
    print("Testing getShelves")
    emptyPantry.addShelf(11, 16)
    testValue = "[{Width: 10; Height: 15}, {Width: 11; Height: 16}]"
    if(str(emptyPantry) != testValue) :
        print("Expected " + testValue + ", returned " + str(emptyPantry))
    else :
        print("getShelves success")
        
    #test getNumShelves
    testValue = 2
    if(emptyPantry.getNumShelves() != testValue) :
        print("Expected " + str(testValue) + ", returned " + str(emptyPantry.getNumShelves()))
    else :
        print("getNumShelves success")
        
    #test search:
        
    
    #test displayShelf():
    testValue = "{Width: 10; Height: 15}"
    if(str(emptyPantry.displayShelf(0)) != testValue) :
        print("Expected " + testValue + ", returned " + str(emptyPantry.displayShelf(0)))
    else :
        print("displayShelf at 0 success")
    testValue = "{Width: 11; Height: 16}"
    if(str(emptyPantry.displayShelf(1)) != testValue) :
        print("Expected " + testValue + ", returned " + str(emptyPantry.displayShelf(0)))
    else :
        print("displayShelf at 1 success")
    
    
