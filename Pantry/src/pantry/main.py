# hello pennapps
import Foodstuff


def driver(pantry, items, shelves):
    pantry = Pantry(len(shelves))
    items_arr = []
    if 'dict' not in str(type(items)):
        for item in len(items):
            items_arr.append(item)
    print("~~~~~~~~~~~~~~\n" + str(items_arr))
# stock = []
# oil = Foodstuff.Foodstuff("olive_oil")
# for i in range(6):
#     stock.append(oil)
# can = Foodstuff.Foodstuff("canned_hash")
# for i in range(8):
#     stock.append(can)
# print(stock)
"""
Output:

Json: {'name': 'California Olive Ranch Arbosana Extra Virgin Olive Oil (16.9 oz)', 'barcode': '850687100018', 'dimensions': {'length': 10.5, 'depth': 3.2, 'height': 2.8, 'weight': 29.6}}
Name: California Olive Ranch Arbosana Extra Virgin Olive Oil (16.9 oz)
Length: 10.5
Depth: 3.2
Height: 3.2
Weight: 29.6
Barcode: 850687100018

"""
