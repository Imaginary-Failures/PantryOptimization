import Foodstuff
import Shelf
import PantrySorter

Foodlist1 = [Foodstuff.Foodstuff('hash'), Foodstuff.Foodstuff('peas'), Foodstuff.Foodstuff('oil')]
# for i in range(6):
#     Foodlist1.append(hash)
Foodlist2 = [Foodstuff.Foodstuff('tomato'), Foodstuff.Foodstuff('flakes'), Foodstuff.Foodstuff('whipped')]
# for i in range(20):
#     Foodlist1.append(hash)
x = PantrySorter.PantrySorterEmptyShelf(Shelf.Shelf(36, 10), Foodlist1, Foodlist2)
print("~~~~~~~~~~~~~~~~~\nOUT\n~~~~~~~~~~~~~~~~~")
for stack in x.getFoodstacks():
    print(stack)
    print(stack.getItems())
