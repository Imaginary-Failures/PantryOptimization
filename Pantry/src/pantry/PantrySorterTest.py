import Foodstuff
import Shelf
import PantrySorter

Foodlist1 = [Foodstuff.Foodstuff('hash'), Foodstuff.Foodstuff('peas'), Foodstuff.Foodstuff('oil')]
Foodlist2 = [Foodstuff.Foodstuff('tomato'), Foodstuff.Foodstuff('flakes'), Foodstuff.Foodstuff('whipped_cream')]
x = PantrySorter.PantrySorterEmptyShelf(Shelf.Shelf(36, 10), Foodlist1, Foodlist2)
print(x.getFoodstacks())