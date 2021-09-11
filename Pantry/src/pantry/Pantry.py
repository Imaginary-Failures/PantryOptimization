from pantry import Shelf

class Pantry():
    def __init__(self):
        self.numShelves = int(input("How many shelves in pantry?"))
        self.shelves = [];
        for s in range(self.numShelves):
            self.shelves.append(Pantry.addShelf(self))
            print(self.shelves)
    pass 

    def addShelf(self):
        length = int(input("Length of shelf: "))
        width = int(input("Width of shelf: "))
        height = int(input("Height of shelf: "))
        newShelf = Shelf.Shelf(length, width, height)
        return newShelf