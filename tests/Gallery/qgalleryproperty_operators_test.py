import unittest

from QtMobility.Gallery import QGalleryProperty, QGalleryMetaDataFilter
from QtMobility.Gallery import QGalleryFilter


class QGalleryPropertyOperatorsTest(unittest.TestCase):

    def setUp(self):
        self.propertyA = QGalleryProperty()
        self.propertyB = QGalleryProperty()
        
    def testLessThanOperator(self):
        f = (self.propertyA < self.propertyB)
        self.assertEquals(f.comparator(), QGalleryFilter.Comparator.LessThan)
    
    def testLessThanEqualsOperator(self):
        f = (self.propertyA <= self.propertyB)
        self.assertEquals(f.comparator(), QGalleryFilter.Comparator.LessThanEquals)
    
    def testEqualsOperator(self):
        f = (self.propertyA == self.propertyB)
        self.assertEquals(f.comparator(), QGalleryFilter.Comparator.Equals)
    
    def testGreaterThanEqualsOperator(self):
        f = (self.propertyA >= self.propertyB)
        self.assertEquals(f.comparator(), QGalleryFilter.Comparator.GreaterThanEquals)
    
    def testGreaterThanOperator(self):
        f = (self.propertyA > self.propertyB)
        self.assertEquals(f.comparator(), QGalleryFilter.Comparator.GreaterThan)


if __name__ == '__main__':
    unittest.main()
