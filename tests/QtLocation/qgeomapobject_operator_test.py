import unittest

from helper import UsesQCoreApplication
from QtMobility.Location import QGeoMapObject

class QGeoMapObjectOperatorTest(UsesQCoreApplication):

    def testOperators(self):
        a = QGeoMapObject()
        b = QGeoMapObject()
        a.setZValue(10)
        # Comparison in QGeoMapObject is done with the Z value
        # Z value is initialized with 0
        self.assert_(a > b)
        self.assertFalse(a < b)

if __name__ == '__main__':
    unittest.main()


