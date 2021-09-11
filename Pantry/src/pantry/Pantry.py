from pantry import Shelf

class Pantry():
    def __init__(self, numShelves=None):
        if(numShelves is None):
            self.numShelves = int(input("How many shelves in pantry?"))
        else:
            self.numShelves = numShelves
        self.shelves = [];
        for s in range(self.numShelves):
            Pantry.addShelf(self)
    pass 

    def addShelf(self, width=None, height=None):
        if(width is None):
            self.width = int(input("Width of shelf: "))
        else:
            self.width = width
        if(height is None):
            height = int(input("Height of shelf: "))
        else:
            self.height = height
        newShelf = Shelf.Shelf(width, height)
        self.shelves.append(newShelf)
        return newShelf
    pass

    def getShelves(self):
        return self.shelves
    pass

    def getNumShelves(self):
        return self.numShelves
    pass

    def search(self, foodstuff):
        for shelf in self.shelves:
            if(shelf.searchFor(foodstuff) != None):
                return shelf.searchFor(foodstuff)
        return None
    pass
    
    def displayShelf(self, index):
        return self.shelves[index]
    pass

    def __str__(self):
        return str(self.shelves)
    pass