#!/usr/bin/python

import unittest
from PySide.QtGui import QApplication
from QtMobility.Contacts import *

class QtContactsUsage(unittest.TestCase):

    def testNewandRetrieveContact(self):
        app = QApplication([])
        cm = QContactManager()

        #Create a new Contact
        exampleContact = QContact()
        nameDetail = QContactName()
        nameDetail.setFirstName("John")
        nameDetail.setLastName("PySide")
        phoneNumberDetail = QContactPhoneNumber()
        phoneNumberDetail.setNumber("+123 4567")
        exampleContact.saveDetail(nameDetail)
        exampleContact.saveDetail(phoneNumberDetail)

        self.assert_(cm.saveContact(exampleContact))

        filtr = QContactLocalIdFilter()
        filtr.add(exampleContact.localId())

        newContact = cm.contacts(filtr)[0]

        surname = newContact.detail(QContactName.DefinitionName).value(QContactName.FieldLastName)
        phone = newContact.detail(QContactPhoneNumber.DefinitionName).value(QContactPhoneNumber.FieldNumber)

        self.assertEqual("PySide", surname)
        self.assertEqual("+123 4567", phone)

        self.assert_(cm.removeContact(exampleContact.localId()))


class PhoneNumberTest(unittest.TestCase):

    def basicTest(self):
        number = QContactPhoneNumber()
        self.assertEqual(number.number(), '')

        subtypes = [QContactPhoneNumber.SubTypeCar, QContactPhoneNumber.SubTypeFax]
        number.setSubTypes(subtypes)
        self.assertEqual(number.subTypes(), subtypes)
        self.assertEqual(number.value(QContactPhoneNumber.FieldSubTypes), subtypes)

if __name__ == '__main__':
    unittest.main()
