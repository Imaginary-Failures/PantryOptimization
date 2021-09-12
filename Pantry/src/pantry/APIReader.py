import json
import os


def getItem(item: str) -> str:
    dir = './Feed/GenericJSONS'
    for filename in os.listdir(dir):
        curr_file = os.path.join(dir, filename)
        if item in filename:
            return "{}/{}".format(dir,filename)


def readFile(file) -> str:
    f = open(file, 'r')
    content = f.read()
    return json.loads(content)


class APIReader:
    """The APIReader class finds the file with a similar name and grabs its JSON"""
    def __init__(self, item_name: str):
        self.filename = getItem(item_name)
        self.r_json = readFile(self.filename)

    def __str__(self):
        return "Filename: {}\nJSON: {}\n".format(self.filename, self.r_json)