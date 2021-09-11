from Feed import APIReader


def volume(length: float, depth: float, height: float):
    return float(length, depth, height)


class Foodstuff:

    def __init__(self, name: str):
        self.d = APIReader.APIReader(name).r_json
        self.name = self.d["name"]
        self.length = self.d["dimensions"]["length"]
        self.depth = self.d["dimensions"]["depth"]
        self.height = self.d["dimensions"]["depth"]
        self.weight = self.d["dimensions"]["weight"]
        self.barcodeID = self.d["barcode"]

    def __str__(self):
        return "Json: {}\nName: {}\nLength: {}\nDepth: {}\nHeight: {}\nWeight: {}\nBarcode: {}\n".format(self.d, self.name, self.length, self.depth, self.height, self.weight, self.barcodeID)