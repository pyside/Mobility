
import unittest


from QtMobility.Gallery import QGalleryFilter, QGalleryMetaDataFilter
from QtMobility.Gallery import QGalleryIntersectionFilter, QGalleryUnionFilter


class IntersectionOperator(unittest.TestCase):

    def testMetaDataIntersection(self):

        metaDataFilter = QGalleryMetaDataFilter()
        intersectionFilter = QGalleryIntersectionFilter()

        intersectionFilter = metaDataFilter and intersectionFilter
        self.assertTrue(intersectionFilter.isValid(), True)
        self.assertFalse(intersectionFilter.isEmpty())
        self.assertEqual(intersectionFilter.filterCount(), 1)

        filters = intersectionFilter.filters()

        self.assertEqual(len(filters), 1)
        self.assertEqual(filters[0].type(), QGalleryFilter.MetaData)

    def testMetaDataUnion(self):

        metaDataFilter = QGalleryMetaDataFilter()
        unionFilter = QGalleryUnionFilter()

        intersectionFilter = metaDataFilter and unionFilter
        self.assertTrue(intersectionFilter.isValid(), True)
        self.assertFalse(intersectionFilter.isEmpty())
        self.assertEqual(intersectionFilter.filterCount(), 2)

        filters = intersectionFilter.filters()

        self.assertEqual(len(filters), 2)
        self.assertEqual(filters[0].type(), QGalleryFilter.MetaData)
        self.assertEqual(filters[1].type(), QGalleryFilter.Union)

    def testUnionMetaData(self):

        metaDataFilter = QGalleryMetaDataFilter()
        unionFilter = QGalleryUnionFilter()

        intersectionFilter = unionFilter and metaDataFilter
        self.assertTrue(intersectionFilter.isValid(), True)
        self.assertFalse(intersectionFilter.isEmpty())
        self.assertEqual(intersectionFilter.filterCount(), 2)

        filters = intersectionFilter.filters()

        self.assertEqual(len(filters), 2)
        self.assertEqual(filters[0].type(), QGalleryFilter.Union)
        self.assertEqual(filters[1].type(), QGalleryFilter.MetaData)

    def testIntersectionMetaData(self):

        metaDataFilter = QGalleryMetaDataFilter()
        unionFilter = QGalleryUnionFilter()

        intersectionFilter = unionFilter and metaDataFilter
        intersectionFilter = intersectionFilter and metaDataFilter

        self.assertTrue(intersectionFilter.isValid(), True)
        self.assertFalse(intersectionFilter.isEmpty())
        self.assertEqual(intersectionFilter.filterCount(), 3)

        filters = intersectionFilter.filters()

        self.assertEqual(len(filters), 3)
        self.assertEqual(filters[0].type(), QGalleryFilter.Union)
        self.assertEqual(filters[1].type(), QGalleryFilter.MetaData)
        self.assertEqual(filters[2].type(), QGalleryFilter.MetaData)


if __name__ == '__main__':
    unittest.main()
