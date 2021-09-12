import Foodstuff
import Shelf
import PantrySorter

Foodlist1 = [Foodstuff.Foodstuff('hash'), Foodstuff.Foodstuff('peas'), Foodstuff.Foodstuff('oil')]
Foodlist2 = [Foodstuff.Foodstuff('tomato'), Foodstuff.Foodstuff('flakes'), Foodstuff.Foodstuff('whipped_cream')]
pantryShelf = Shelf.Shelf(36, 10)
x = PantrySorter.PantrySorterEmptyShelf(pantryShelf, Foodlist1, Foodlist2)
x = PantrySorter.PantrySorterDynamicShelf(pantryShelf, Foodstuff.Foodstuff('baking_soda'))
for stack in x.getFoodstacks():
    print(stack)
    print(stack.getItems())
