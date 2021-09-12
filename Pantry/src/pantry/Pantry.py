import Shelf
import Stack

class Pantry:
    def __init__(self, numShelves=None):
        if(numShelves is None):
            numShelves = int(input("How many shelves in pantry?"))
        else:
            numShelves = numShelves
        self.shelves = [];
        for s in range(numShelves):
            Pantry.addShelf(self)
    pass 

    def addShelf(self, w=None, h=None):
        if(w is None):
            w = int(input("Width of shelf: "))
        if(h is None):
            h = int(input("Height of shelf: "))
        newShelf = Shelf.Shelf(w, h)
        self.shelves.append(newShelf)
        return newShelf
    pass

    def getShelves(self):
        return self.shelves
    pass

    def getNumShelves(self):
        return len(self.shelves)
    pass
    
    def displayShelf(self, index):
        return self.shelves[index]
    pass

    def __str__(self):
        return str(self.shelves)
    pass