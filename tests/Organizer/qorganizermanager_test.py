import unittest
from helper import UsesQCoreApplication
from QtMobility.Organizer import *

class QOrganizerItemTest(UsesQCoreApplication):

    def setUp(self):
        UsesQCoreApplication.setUp(self)
        self.itemAdded = False
        self.itemRemoved = False
        self.itemChanged = False

    def tearDown(self):
        UsesQCoreApplication.tearDown(self)

    def itemsAddedCallback(self):
        self.itemAdded = True

    def itemsRemovedCallback(self):
        self.itemRemoved = True

    def itemsChangedCallback(self):
        self.itemChanged = True

    def testManager(self):
        manager = QOrganizerManager()
        manager.itemsAdded.connect(self.itemsAddedCallback)
        manager.itemsRemoved.connect(self.itemsRemovedCallback)
        manager.itemsChanged.connect(self.itemsChangedCallback)
        initialEntries = len(manager.items())
        
        journal = QOrganizerJournal()
        journal.setDescription("This is a sample journal, it can be safely deleted")
        self.assert_(manager.saveItem(journal))
        self.assertEquals(len(manager.items()), initialEntries + 1)
        
        journal.addComment("And this is just a comment that was added")
        self.assert_(manager.saveItem(journal))

        manager.removeItem(journal.id())
        self.assertEquals(len(manager.items()), initialEntries)
        
        self.assert_(self.itemAdded)
        self.assert_(self.itemRemoved)
        self.assert_(self.itemChanged)

   

if __name__ == '__main__':
    unittest.main()
