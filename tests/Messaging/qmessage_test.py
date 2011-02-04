import unittest
from helper import UsesQApplication
from QtMobility.Messaging import *
from PySide.QtCore import *


class QMessageTest(UsesQApplication):

    def testHeaderFields(self):
        msg = QMessage()
        self.assertEquals(len(msg.headerFields()), 0)
        self.assertEquals(len(msg.headerFieldValues("Subject")), 0)
        self.assertEquals(len(msg.headerFieldValues("From")), 0)
        self.assertEquals(len(msg.headerFieldValues("To")), 0)
        self.assertEquals(len(msg.headerFieldValues("X-None")), 0)
        self.assertEquals(len(msg.headerFieldValue("Subject")), 0)
        self.assertEquals(len(msg.headerFieldValue("From")), 0)
        self.assertEquals(len(msg.headerFieldValue("To")), 0)
        self.assertEquals(len(msg.headerFieldValue("X-None")), 0)

    def testPriority(self):
        msg = QMessage()
        self.assertEquals(msg.priority(), QMessage.NormalPriority)
        self.assertEquals(msg.isModified(), False)

        msg.setPriority(QMessage.HighPriority)
        self.assertEquals(msg.priority(), QMessage.HighPriority)
        self.assertTrue(msg.isModified())

        msg.setPriority(QMessage.LowPriority)
        self.assertEquals(msg.priority(), QMessage.LowPriority)

    def testType(self):
        msg = QMessage()
        self.assertEquals(msg.type(), QMessage.NoType)
        self.assertEquals(msg.isModified(), False)

        msg.setType(QMessage.Email)
        self.assertEquals(msg.type(), QMessage.Email)
        self.assertTrue(msg.isModified())

        msg.setType(QMessage.Mms)
        self.assertEquals(msg.type(), QMessage.Mms)

    def testSubject(self):
        msg = QMessage()
        self.assertEquals(msg.subject(), "")
        self.assertEquals(msg.isModified(), False)

        subject = "Short subject"
        msg.setSubject(subject)
        self.assertEquals(msg.subject(), subject)
        self.assertTrue(msg.isModified())

        subject = "A longer subject, just to try to make this test more interesting"
        msg.setSubject(subject)
        self.assertEquals(msg.subject(), subject)

    def testFrom(self):
        msg = QMessage()
        self.assertEquals(msg.from_(), QMessageAddress())
        self.assertEquals(msg.isModified(), False)

        addr = QMessageAddress(QMessageAddress.Email, "alice@example.org")
        msg.setFrom(addr)
        self.assertEquals(msg.from_(), addr)
        self.assertTrue(msg.from_() != QMessageAddress())
        self.assertTrue(msg.isModified())

        addr = QMessageAddress(QMessageAddress.InstantMessage, "bob@example.org")
        msg.setFrom(addr)
        self.assertEquals(msg.from_(), addr)
        self.assertTrue(msg.from_() != QMessageAddress())


    def testTo(self):
        msg = QMessage()
        self.assertEquals(msg.to(), [])
        self.assertEquals(msg.isModified(), False)

        addresses = []
        addresses.append(QMessageAddress(QMessageAddress.Email, "alice@example.org"))
        addresses.append(QMessageAddress(QMessageAddress.Email, "bob@example.org"))

        msg.setTo(addresses)
        self.assertEquals(msg.to(), addresses)
        self.assertTrue(msg.isModified())

        addresses = []
        addresses.append(QMessageAddress(QMessageAddress.System, "charlie@example.org"))
        msg.setTo(addresses)
        self.assertEquals(msg.to(), addresses)


    def testCc(self):
        msg = QMessage()
        self.assertEquals(msg.cc(), [])
        self.assertEquals(msg.isModified(), False)

        addresses = []
        addresses.append(QMessageAddress(QMessageAddress.Email, "alice@example.org"))
        addresses.append(QMessageAddress(QMessageAddress.Email, "bob@example.org"))

        msg.setCc(addresses)
        self.assertEquals(msg.cc(), addresses)
        self.assertTrue(msg.isModified())

        addresses = []
        addresses.append(QMessageAddress(QMessageAddress.System, "charlie@example.org"))
        msg.setCc(addresses)
        self.assertEquals(msg.cc(), addresses)

    def testBcc(self):
        msg = QMessage()
        self.assertEquals(msg.bcc(), [])
        self.assertEquals(msg.isModified(), False)

        addresses = []
        addresses.append(QMessageAddress(QMessageAddress.Email, "alice@example.org"))
        addresses.append(QMessageAddress(QMessageAddress.Email, "bob@example.org"))

        msg.setBcc(addresses)
        self.assertEquals(msg.bcc(), addresses)
        self.assertTrue(msg.isModified())

        addresses = []
        addresses.append(QMessageAddress(QMessageAddress.System, "charlie@example.org"))
        msg.setBcc(addresses)
        self.assertEquals(msg.bcc(), addresses)

    def testDate(self):
        msg = QMessage()
        self.assertEquals(msg.date(), QDateTime())
        self.assertEquals(msg.isModified(), False)

        now = QDateTime(QDateTime.fromString(QDateTime.currentDateTime().toString(Qt.ISODate), Qt.ISODate))
        msg.setReceivedDate(now)
        self.assertEquals(msg.receivedDate(), now)
        self.assertTrue(msg.isModified())

        now = QDateTime.fromString("2000-01-01T00:00:01Z", Qt.ISODate)
        msg.setReceivedDate(now)
        self.assertEquals(msg.receivedDate(), now)



if __name__ == '__main__':
    unittest.main()
