import unittest
from PySide.QtCore import QUrl
from PySide.QtNetwork import QNetworkRequest
from QtMobility.MultimediaKit import QMediaContent, QMediaResource


class QMediaContentTest(unittest.TestCase):
    def testNull(self):
        media = QMediaContent()
        self.assert_(media.isNull())
        self.assertEqual(media.canonicalUrl(), QUrl())
        self.assertEqual(media.canonicalResource(), QMediaResource())
        self.assertEqual(media.resources(), [])

    def testUrlCtor(self):
        media = QMediaContent(QUrl('http://example.com/movie.mov'))
        self.assertEqual(media.canonicalUrl(), QUrl('http://example.com/movie.mov'))
        self.assertEqual(media.canonicalResource().url(), QUrl('http://example.com/movie.mov'))

    def testRequestCtor(self):
        request = QNetworkRequest(QUrl('http://example.com/movie.mov'))
        request.setAttribute(QNetworkRequest.User, 1234)

        media = QMediaContent(request)

        self.assertEqual(media.canonicalUrl(), QUrl('http://example.com/movie.mov'))
        self.assertEqual(media.canonicalResource().request(), request)
        self.assertEqual(media.canonicalResource().url(), QUrl('http://example.com/movie.mov'))

    def testResourceCtor(self):
        media = QMediaContent(QMediaResource(QUrl('http://example.com/movie.mov')))
        self.assertEqual(media.canonicalResource(), QMediaResource(QUrl('http://example.com/movie.mov')))

    def testResourceListCtor(self):
        resourceList = [QMediaResource(QUrl('http://example.com/movie.mov'))]
        media = QMediaContent(resourceList)
        self.assertEqual(media.canonicalUrl(), QUrl('http://example.com/movie.mov'))
        self.assertEqual(media.canonicalResource().url(), QUrl('http://example.com/movie.mov'))

    def testCopy(self):
        media1 = QMediaContent(QMediaResource(QUrl('http://example.com/movie.mov')))
        media2 = QMediaContent(media1)
        self.assertEqual(media1, media2)

    def testAssignment(self):
        media1 = QMediaContent(QMediaResource(QUrl('http://example.com/movie.mov')))
        media2 = QMediaContent()
        media3 = QMediaContent()

        media2 = media1
        self.assertEqual(media2, media1)

        media2 = media3
        self.assertEqual(media2, media3)


    def testEquality(self):
        ''' Test operators '==' and '!='.'''
        media1 = QMediaContent()
        media2 = QMediaContent()
        media3 = QMediaContent(QMediaResource(QUrl('http://example.com/movie.mov')))
        media4 = QMediaContent(QMediaResource(QUrl('http://example.com/movie.mov')))
        media5 = QMediaContent(QMediaResource(QUrl('file:///some/where/over/the/rainbow.mp3')))

        # '==' and '!=' operators -- null == null
        self.assert_(media1 == media2)
        self.assertFalse(media1 != media2)

        # '==' and '!=' operators -- null != something
        self.assertFalse(media1 == media3)
        self.assert_(media1 != media3)

        # equiv
        self.assert_(media3 == media4)
        self.assertFalse(media3 != media4)

        # not equiv
        self.assertFalse(media4 == media5)
        self.assert_(media4 != media5)

    def testResources(self):
        resourceList = [QMediaResource(QUrl('http://example.com/movie-main.mov')),
                        QMediaResource(QUrl('http://example.com/movie-big.mov'))]
        media = QMediaContent(resourceList)
        res = media.resources();
        self.assertEqual(len(res), 2)
        self.assertEqual(res[0], QMediaResource(QUrl('http://example.com/movie-main.mov')))
        self.assertEqual(res[1], QMediaResource(QUrl('http://example.com/movie-big.mov')))


if __name__ == '__main__':
    unittest.main()

