
import unittest

from PySide.QtCore import *
from QtMobility.PublishSubscribe import *

from helper import UsesQCoreApplication

class Publisher(object):
    def __init__(self):
        self.publisher = QValueSpacePublisher(QValueSpace.WritableLayer, '/foobar')
        self.value = 0
        self.publisher.setValue('intValue', self.value)

    def updateValue(self, value):
        self.value = value
        self.publisher.setValue('intValue', self.value)


class Subscriber(QObject):
    def __init__(self, connection_mode=0):
        QObject.__init__(self)
        self.publisherValue = None
        self.subscriber = QValueSpaceSubscriber('/foobar', self)
        if connection_mode == 0:
            QObject.connect(self.subscriber, SIGNAL('contentsChanged()'), self, SLOT('subscriberChanged()'))
        elif connection_mode == 1:
            QObject.connect(self.subscriber, SIGNAL('contentsChanged()'), self.subscriberChanged())
        elif connection_mode == 2:
            self.subscriber.contentsChanged.connect(self.subscriberChanged)

    def subscriberChanged(self):
        subPaths = self.subscriber.subPaths()
        self.publisherValue = self.subscriber.value(subPaths[0])


class PublishSubscriberTest(UsesQCoreApplication):

    def setUp(self):
        #Acquire resources
        QValueSpace.initValueSpaceServer()
        self.timer = QTimer()
        UsesQCoreApplication.setUp(self)

    def tearDown(self):
        #Release resources
        del self.timer
        UsesQCoreApplication.tearDown(self)

    def testPublishSubscribeWithOldStyleConnection(self):
        publisher = Publisher()
        subscriber = Subscriber()

        def modifyPublisherValue():
            publisher.updateValue(1234)
            self.app.exit(0)

        QObject.connect(self.timer, SIGNAL('timeout()'), modifyPublisherValue)
        self.timer.start(4)

        self.app.exec_()

    def testPublishSubscribeWithOldStyleConnectionAndCallback(self):
        publisher = Publisher()
        subscriber = Subscriber(1)

        def modifyPublisherValue():
            publisher.updateValue(1234)
            self.app.exit(0)

        QObject.connect(self.timer, SIGNAL('timeout()'), modifyPublisherValue)
        self.timer.start(4)

        self.app.exec_()

    def testPublishSubscribeWithNewStyleConnection(self):
        publisher = Publisher()
        subscriber = Subscriber(2)

        def modifyPublisherValue():
            publisher.updateValue(1234)
            self.app.exit(0)

        QObject.connect(self.timer, SIGNAL('timeout()'), modifyPublisherValue)
        self.timer.start(4)

        self.app.exec_()

if __name__ == '__main__':
    unittest.main()

