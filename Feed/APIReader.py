import json
import os


def getItem(item: str):
    dir = './GenericJSONS'
    for filename in os.listdir(dir):
        # print(str(filename))
        curr_file = os.path.join(dir, filename)
        if item in filename:
            return "{}/{}".format(dir,filename)


def readFile(file):
    f = open(file, 'r')
    content = f.read()
    return json.loads(content)


class APIReader:

    def __init__(self, item_name: str):
        self.filename = getItem(item_name)
        self.r_json = readFile(self.filename)

    def createDict(self):
        pass

    def __str__(self):
        return "Filename: {}\nJSON: {}\n".format(self.filename, self.r_json)