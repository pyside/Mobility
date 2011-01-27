import unittest


from QtMobility.Gallery import QGalleryFilter, QGalleryMetaDataFilter
from QtMobility.Gallery import QGalleryIntersectionFilter, QGalleryUnionFilter


class CopyTest(unittest.TestCase):

    def testCopyMetaData(self):
        metaDataFilter = QGalleryMetaDataFilter()
        filt = QGalleryFilter(metaDataFilter)

        self.assertTrue(filt.isValid())
        self.assertEqual(filt.type(), QGalleryFilter.MetaData)

    def testCopyIntersection(self):
        intersectionFilter = QGalleryIntersectionFilter()
        filt = QGalleryFilter(intersectionFilter)

        self.assertTrue(filt.isValid())
        self.assertEqual(filt.type(), QGalleryFilter.Intersection)

    def testCopyUnion(self):
        unionFilter = QGalleryUnionFilter()
        filt = QGalleryFilter(unionFilter)

        self.assertTrue(filt.isValid())
        self.assertEqual(filt.type(), QGalleryFilter.Union)


if __name__ == '__main__':
    unittest.main()
