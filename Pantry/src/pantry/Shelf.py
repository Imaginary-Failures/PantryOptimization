class Shelf:
    
    def __init__(self, w, h):
        self.width = w
        self.height = h
    pass

    def __str__(self):
        return '' + str(self.width) + ', ' + str(self.height)
    def __repr__(self):
        return '' + str(self.width) + ', ' + str(self.height)
    