import unittest

from QtMobility.Gallery import QGalleryFilter, QGalleryMetaDataFilter
from QtMobility.Gallery import QGalleryIntersectionFilter, QGalleryUnionFilter


class UnionFilterEmpty(unittest.TestCase):

    def testEmpty(self):
        unionFilter = QGalleryUnionFilter()

        self.assertTrue(unionFilter.isValid(), True)
        self.assertTrue(unionFilter.isEmpty(), True)
        self.assertEqual(unionFilter.filterCount(), 0)


class UnionFilterAppend(unittest.TestCase):

    def testAppendMetaData(self):
        unionFilter = QGalleryUnionFilter()

        metaDataFilter = QGalleryMetaDataFilter()
        intersectionFilter = QGalleryIntersectionFilter()

        unionFilter.append(metaDataFilter)
        unionFilter.append(metaDataFilter)
        unionFilter.append(intersectionFilter)
        unionFilter.append(metaDataFilter)
        self.assertFalse(unionFilter.isEmpty())
        self.assertEqual(unionFilter.filterCount(), 4)

        filters = unionFilter.filters()
        self.assertEqual(len(filters), 4)

        self.assertEqual(filters[0].type(), QGalleryFilter.MetaData)
        self.assertEqual(filters[1].type(), QGalleryFilter.MetaData)
        self.assertEqual(filters[2].type(), QGalleryFilter.Intersection)
        self.assertEqual(filters[3].type(), QGalleryFilter.MetaData)

    def testAppendUnion(self):

        unionFilter = QGalleryUnionFilter()

        metaDataFilter = QGalleryMetaDataFilter()
        intersectionFilter = QGalleryIntersectionFilter()

        unionFilter.append(metaDataFilter)
        unionFilter.append(metaDataFilter)
        unionFilter.append(intersectionFilter)
        unionFilter.append(metaDataFilter)

        # Should append the *contents* of the union filter
        unionFilter.append(unionFilter)
        self.assertFalse(unionFilter.isEmpty())
        self.assertEqual(unionFilter.filterCount(), 8)

        self.assertEqual(filters[0].type(), QGalleryFilter.MetaData)
        self.assertEqual(filters[1].type(), QGalleryFilter.MetaData)
        self.assertEqual(filters[2].type(), QGalleryFilter.Intersection)
        self.assertEqual(filters[3].type(), QGalleryFilter.MetaData)

        self.assertEqual(filters[4].type(), QGalleryFilter.MetaData)
        self.assertEqual(filters[5].type(), QGalleryFilter.MetaData)
        self.assertEqual(filters[6].type(), QGalleryFilter.Intersection)
        self.assertEqual(filters[7].type(), QGalleryFilter.MetaData)


class UnionFilterPrepend(unittest.TestCase):

    def testPrependMetaData(self):
        unionFilter = QGalleryUnionFilter()

        metaDataFilter = QGalleryMetaDataFilter()
        intersectionFilter = QGalleryIntersectionFilter()

        unionFilter.append(metaDataFilter)
        unionFilter.append(intersectionFilter)

        unionFilter.prepend(metaDataFilter)
        unionFilter.prepend(intersectionFilter)


        self.assertFalse(unionFilter.isEmpty())
        self.assertEqual(unionFilter.filterCount(), 4)

        filters = unionFilter.filters()
        self.assertEqual(len(filters), 4)

        self.assertEqual(filters[0].type(), QGalleryFilter.Intersection)
        self.assertEqual(filters[1].type(), QGalleryFilter.MetaData)
        self.assertEqual(filters[2].type(), QGalleryFilter.MetaData)
        self.assertEqual(filters[3].type(), QGalleryFilter.Intersection)

    def testPrependUnion(self):

        unionFilter = QGalleryUnionFilter()

        metaDataFilter = QGalleryMetaDataFilter()
        intersectionFilter = QGalleryIntersectionFilter()

        unionFilter.append(metaDataFilter)
        unionFilter.append(metaDataFilter)
        unionFilter.append(intersectionFilter)
        unionFilter.append(metaDataFilter)

        # Should append the *contents* of the union filter
        unionFilter.prepend(unionFilter)
        self.assertFalse(unionFilter.isEmpty())
        self.assertEqual(unionFilter.filterCount(), 8)

        self.assertEqual(filters[0].type(), QGalleryFilter.MetaData)
        self.assertEqual(filters[1].type(), QGalleryFilter.MetaData)
        self.assertEqual(filters[2].type(), QGalleryFilter.Intersection)
        self.assertEqual(filters[3].type(), QGalleryFilter.MetaData)

        self.assertEqual(filters[4].type(), QGalleryFilter.MetaData)
        self.assertEqual(filters[5].type(), QGalleryFilter.MetaData)
        self.assertEqual(filters[6].type(), QGalleryFilter.Intersection)
        self.assertEqual(filters[7].type(), QGalleryFilter.MetaData)


class UnionFilterInsert(unittest.TestCase):

    def testInsert(self):
        unionFilter =  QGalleryUnionFilter()

        metaDataFilter = QGalleryMetaDataFilter()
        intersectionFilter = QGalleryIntersectionFilter()

        unionFilter.append(metaDataFilter)
        unionFilter.append(metaDataFilter)
        unionFilter.append(intersectionFilter)
        unionFilter.append(metaDataFilter)

        # Inserts at the given position and shift the existing
        # filters, extending the filter list
        unionFilter.insert(1, intersectionFilter)
        unionFilter.insert(2, metaDataFilter)

        self.assertEqual(unionFilter.isEmpty(), False)
        self.assertEqual(unionFilter.filterCount(), 6)

        filters = unionFilter.filters()

        self.assertEqual(filters[0].type(), QGalleryFilter.MetaData)
        self.assertEqual(filters[1].type(), QGalleryFilter.Intersection)
        self.assertEqual(filters[2].type(), QGalleryFilter.MetaData)
        self.assertEqual(filters[3].type(), QGalleryFilter.MetaData)
        self.assertEqual(filters[4].type(), QGalleryFilter.Intersection)
        self.assertEqual(filters[5].type(), QGalleryFilter.MetaData)


class UnionFilterReplace(unittest.TestCase):

    def testReplace(self):
        unionFilter =  QGalleryUnionFilter()

        metaDataFilter = QGalleryMetaDataFilter()
        intersectionFilter = QGalleryIntersectionFilter()

        unionFilter.append(metaDataFilter)
        unionFilter.append(metaDataFilter)
        unionFilter.append(intersectionFilter)
        unionFilter.append(metaDataFilter)

        unionFilter.replace(0, intersectionFilter)
        unionFilter.replace(2, metaDataFilter)

        self.assertEqual(unionFilter.isEmpty(), False)
        self.assertEqual(unionFilter.filterCount(), 4)

        filters = unionFilter.filters()

        self.assertEqual(filters[0].type(), QGalleryFilter.Intersection)
        self.assertEqual(filters[1].type(), QGalleryFilter.MetaData)
        self.assertEqual(filters[2].type(), QGalleryFilter.MetaData)
        self.assertEqual(filters[3].type(), QGalleryFilter.MetaData)


class UnionFilterRemove(unittest.TestCase):

    def testReplace(self):
        unionFilter =  QGalleryUnionFilter()

        metaDataFilter = QGalleryMetaDataFilter()
        intersectionFilter = QGalleryIntersectionFilter()

        unionFilter.append(metaDataFilter)
        unionFilter.append(intersectionFilter)
        unionFilter.append(metaDataFilter)
        unionFilter.append(intersectionFilter)

        unionFilter.remove(0)
        unionFilter.remove(1)

        self.assertEqual(unionFilter.isEmpty(), False)
        self.assertEqual(unionFilter.filterCount(), 2)

        filters = unionFilter.filters()

        self.assertEqual(filters[0].type(), QGalleryFilter.Intersection)
        self.assertEqual(filters[1].type(), QGalleryFilter.Intersection)


class UnionFilterClear(unittest.TestCase):

    def testReplace(self):
        unionFilter =  QGalleryUnionFilter()

        metaDataFilter = QGalleryMetaDataFilter()
        intersectionFilter = QGalleryIntersectionFilter()

        unionFilter.append(metaDataFilter)
        unionFilter.append(intersectionFilter)
        unionFilter.append(metaDataFilter)
        unionFilter.append(intersectionFilter)

        unionFilter.clear()

        self.assertEqual(unionFilter.isEmpty(), True)
        self.assertEqual(unionFilter.filterCount(), 0)


if __name__ == '__main__':
    unittest.main()
