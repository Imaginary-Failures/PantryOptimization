import Pantry
import Stack
import Shelf
import Foodstuff
from operator import attrgetter


def PantrySorterEmptyShelf(Shelf: Shelf, stackableFood, unstackableFood):
    """
    input an empty shelf, two lists, one of stackable, one of unstackable items
    first seperate into stackable and non stackable items
    make it such that widest, stackable items are at the bottom
    and the last item should be a non stackable item. so we get rid of them
    (if we are left with unstackable items at the end it would be annoying)
    """
    print(stackableFood, unstackableFood)
    unstackableFood = sorted(unstackableFood)
    stackableFood = sorted(stackableFood)
    print("sorted\n{}\n{}".format(unstackableFood, stackableFood))
    iShelf = 0
    remainingWidth = Shelf.width
    while stackableFood and unstackableFood:  # and not Shelf.full
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
                        remainingWidth -= food.depth
                        curStack.addItem(food)
                        print("adding {}".format(food))
                else:
                    curStack.addItem(food)
        for food in curStack.items:
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
                        curStack.addItem(food, stackable=False)
                        unstackableFood.remove(food)
                        break
                else:
                    curStack.addItem(food, stackable=False)
                    unstackableFood.remove(food)
                    break
        iShelf += 1
        try:
            if remainingWidth < stackableFood[-1].depth and remainingWidth < unstackableFood[-1].depth:
                # checks if not even the smallest items in both lists fit onto shelf.
                Shelf.full = True
        except:
            print("avoided something")
    print("end")
    return Shelf


class PantrySorter:
    def __init__(self):
        pass
