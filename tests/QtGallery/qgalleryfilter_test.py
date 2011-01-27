

import unittest


from QtMobility.Gallery import QGalleryFilter, QGalleryMetaDataFilter
from QtMobility.Gallery import QGalleryIntersectionFilter, QGalleryUnionFilter


class NullFilter(unittest.TestCase):

    def testNullFilter(self):
        filt = QGalleryFilter()

        self.assertEqual(filt.type(), QGalleryFilter.Invalid)
        self.assertFalse(filt.isValid())


class MetaDataFilter(unittest.TestCase):

    def testMetaDataFilter(self):

        filt = QGalleryMetaDataFilter()

        self.assertTrue(filt.isValid())
        self.assertEqual(filt.propertyName(), '')
        self.assertEqual(filt.value(), None)
        self.assertEqual(filt.comparator(), QGalleryFilter.Equals)
        self.assertFalse(filt.isNegated())

        propertyName = 'album title'
        value = 'Greatest'
        comparator = QGalleryFilter.StartsWith
        negated = True 

        filt.setPropertyName(propertyName)
        filt.setValue(value)
        filt.setComparator(comparator)
        filt.setNegated(negated)

        self.assertTrue(filt.isValid())
        self.assertEqual(filt.propertyName(), propertyName) 
        self.assertEqual(filt.value(), value)
        self.assertEqual(filt.comparator(), comparator)
        self.assertEqual(filt.isNegated(), negated)


if __name__ == '__main__':
    unittest.main()
