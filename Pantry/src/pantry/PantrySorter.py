import Pantry
import Stack
import Shelf
import Foodstuff
from operator import attrgetter


def printStacks(x):
    print("\n**********\nPrintstacks\n")
    for stack in x.getFoodstacks():
        print(stack)
        print(stack.getItems())



def PantrySorterEmptyShelf(Shelf: Shelf, stackableFood, unstackableFood):
    """
    input an empty shelf, two lists, one of stackable, one of unstackable items
    first separate into stackable and non stackable items
    make it such that widest, stackable items are at the bottom
    and the last item should be a non stackable item. so we get rid of them
    (if we are left with unstackable items at the end it would be annoying)
    """
    print(stackableFood, unstackableFood)
    unstackableFood = sorted(unstackableFood, reverse=True)
    stackableFood = sorted(stackableFood, reverse=True)
    print("sorted\n{}\n{}".format(unstackableFood, stackableFood))
    for foodList in [unstackableFood, stackableFood]:
        for food in foodList:
            if(food.height >= Shelf.height):
                #can never be added because doesn't fit on Shelf
                print("Could not add {} due to exceeding height of Shelf.".format(food))
                foodList.remove(food)
    iShelf = 0
    remainingWidth = Shelf.width

    while (not Shelf.isFull() and (len(stackableFood) != 0 or len(unstackableFood) != 0)) :

        Shelf.createStack()
        print("stack created")
        # here I am trying to get the ith stack on the shelf. but it didnt work for me. It was an object of type list(?)
        curStack = Shelf.stacks[iShelf]
        for food in stackableFood:
            # adds as many stackable food items to stack as possible
            if Shelf.height > curStack.height + food.height:
                # if this is not true, it cant be stacked anyways
                if not curStack.items:
                    # just first item in stack
                    if food.depth < remainingWidth:
                        curStack.addItem(food)
                        print("adding {}".format(food))
                else:
                    curStack.addItem(food)
                remainingWidth -= food.depth
        for food in curStack.items:#remove items that have been shelved
            stackableFood.remove(food)
        removeThisFromUnstackable = None
        for food in unstackableFood:
            # adds as a non stackable food item to stack if possible
            if curStack.stackable and Shelf.height > curStack.height + food.height:
                # if this is not true, it cant be stacked anyways
                if not curStack.items:
                    # just first item in stack
                    if food.depth < remainingWidth:
                        remainingWidth -= food.depth
                        curStack.addItem(food, False)
                        unstackableFood.remove(food)
                        break
                else:
                    curStack.addItem(food, False)
                    unstackableFood.remove(food)
                    break

        iShelf += 1  
        try:
            if(len(stackableFood) != 0 and remainingWidth < stackableFood[-1].depth):
                if(len(unstackableFood) != 0 and remainingWidth < unstackableFood[-1].depth):
                    Shelf.setFull(True)
            elif(len(unstackableFood) != 0 and remainingWidth < unstackableFood[-1].depth):
                if(len(unstackableFood) != 0 and remainingWidth < unstackableFood[-1].depth):
                    Shelf.setFull(True)    
                 # checks if not even the smallest items in both lists fit onto shelf.        
        except:
            print("avoided something")
    print("end")
    return Shelf

"""
DynamicShelf is able to take in a single Foodstuff and scan the stacks of a Shelf 
to check for where the item can be placed. The item will be inserted by width.
"""
def PantrySorterDynamicShelf(Shelf: Shelf, food):
    isAdded = False
    if(not food.isStackable()):
        #find stack whose top item can be stacked on and has sufficient height
        for curStack in Shelf.stacks :
            if curStack.isStackable() and Shelf.height > curStack.height + food.height:
                curStack.addItem(food, False)#change stackable property to False
                isAdded = True
    elif (food.isStackable()):
        #search for suitable Stack and insert
        for curStack in Shelf.stacks:
            if Shelf.height > curStack.height + food.height:
                if (curStack.width < food.depth and remainingWidth > food.depth) :
                #if food to add will become new base and
                #don't add if new base would exceed Shelf width
                    remainingWidth -= (food.depth - curStack.width)
                    curStack.width = food.depth
                    curStack.addItem(food)
                    isAdded = True
                    sorted(curStack.items, reverse=True)
                elif (curStack.width > food.depth):
                    curStack.addItem(food)
                    isAdded = True
                    sorted(curStack.items, reverse=True)
    elif(not isAdded and remainingWidth > food.depth) :
        #create a new Stack and add as first item
        curStack = Shelf.createStack()
        curStack.addItem(food)
        isAdded = True
    else:
        print("Could not be added due to insufficient space.")
    if(isAdded) :
        print("Success adding")
    return Shelf
    
class PantrySorter:
    def __init__(self):
        pass
