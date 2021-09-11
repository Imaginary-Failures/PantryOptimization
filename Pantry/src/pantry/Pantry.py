from pantry import Shelf

class Pantry():
    def __init__(self):
        self.numShelves = int(input("How many shelves in pantry?"))
        self.shelves = [];
        for s in range(self.numShelves):
            self.shelves.append(Pantry.addShelf(self))
    pass 

    def addShelf(self):
        width = int(input("Width of shelf: "))
        height = int(input("Height of shelf: "))
        newShelf = Shelf.Shelf(width, height)
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