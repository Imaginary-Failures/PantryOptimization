from pantry import Pantry, Shelf
import unittest

class PantryTest(unittest.TestCase):
    
    def setUp(self):
        global testPantry
        testPantry = Pantry.Pantry(2)
        global emptyPantry
        emptyPantry = Pantry.Pantry(0)
    pass
    
    def testInit(self):
        comparePantry = Pantry.Pantry()
        ##pass input of 2
        unittest.assertEqual(comparePantry, testPantry)
        pass

    def testAddShelf(self):
        
        pass
    
    def testGetShelves(self):
        
        pass
    
    def testGetNumShelves(self):
        
        pass
    
    def testSearch(self):
        
        pass
    
    def testDisplayShelf(self):
        
        pass
    
    def testStr(self):
        
        pass
    
    
