import unittest

from helper import UsesQCoreApplication
from QtMobility.Location import QGeoPositionInfo
from PySide.QtCore import QDateTime

class TestCase(UsesQCoreApplication):

    def testSetTimestampFunction(self):
        dt = QDateTime.currentDateTime()
        posinfo = QGeoPositionInfo()
        posinfo.setTimestamp(dt)
        self.assertEqual(dt, posinfo.timestamp())

if __name__ == '__main__':
    unittest.main()


