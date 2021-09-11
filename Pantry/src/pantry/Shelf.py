class Shelf:
    
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h
    pass

    def __str__(self):
        return '' + str(self.length) + ', ' + str(self.width) + ', ' + str(self.height)
    def __repr__(self):
        return '' + str(self.length) + ', ' + str(self.width) + ', ' + str(self.height)
    