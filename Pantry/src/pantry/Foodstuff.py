import APIReader


def volume(length: float, depth: float, height: float) -> float:
    return float(length, depth, height)


class Foodstuff:
    """This function creates and hold item information grabbed from the API"""

    def __init__(self, name: str):
        self.d = APIReader.APIReader(name).r_json
        self.name = self.d["name"]
        self.length = self.d["dimensions"]["length"]
        self.depth = self.d["dimensions"]["depth"]
        self.height = self.d["dimensions"]["height"]
        self.weight = self.d["dimensions"]["weight"]
        self.barcodeID = self.d["barcode"]
        self.type = self.d["dimensions"]["type"]

    def isStackable(self) -> bool:
        non_stackable = ["bottle", "special", "small"]  # need more examples of non-stackables
        return self.type not in non_stackable

    def __str__(self):
        return "Json: {}\nName: {}\nDepth: {}\nHeight: {}\nType: {}\nStackable: {}".format(
            self.d,
            self.name,
            # self.length,
            self.depth,
            self.height,
            # self.weight,
            # self.barcodeID,
            self.type, self.isStackable())

    def __le__(self, other):
        print("Less equal")

    def __lt__(self, other):

        temp = self.depth < other.depth
        print("Computed {} < {}: {}".format(self.depth, other.depth, temp))
        return temp

