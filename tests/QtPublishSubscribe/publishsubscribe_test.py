
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
    def __init__(self, connection_mode, app):
        QObject.__init__(self)

        self.publisherValue = None
        self.app = app
        self.subscriber = QValueSpaceSubscriber('/foobar', self)

        if connection_mode == 0:
            QObject.connect(self.subscriber, SIGNAL('contentsChanged()'), self, SLOT('subscriberChanged()'))
        elif connection_mode == 1:
            QObject.connect(self.subscriber, SIGNAL('contentsChanged()'), self.subscriberChanged)
        elif connection_mode == 2:
            self.subscriber.contentsChanged.connect(self.subscriberChanged)

    def subscriberChanged(self):
        subPaths = self.subscriber.subPaths()
        self.publisherValue = self.subscriber.value(subPaths[0])
        self.app.exit(0)


value_space_server_initialised = False

class PublishSubscriberTest(UsesQCoreApplication):

    def setUp(self):
        #Acquire resources
        global value_space_server_initialised
        if not value_space_server_initialised:
            QValueSpace.initValueSpaceServer()
            value_space_server_initialised = True
        UsesQCoreApplication.setUp(self)

    def testPublishSubscribeWithOldStyleConnection(self):
        publisher = Publisher()
        subscriber = Subscriber(0, self.app)
        value = 123
        publisher.updateValue(value)
        self.app.exec_()
        self.assertEqual(subscriber.publisherValue, value)

    def testPublishSubscribeWithOldStyleConnectionAndCallback(self):
        publisher = Publisher()
        subscriber = Subscriber(1, self.app)
        value = 456
        publisher.updateValue(value)
        self.app.exec_()
        self.assertEqual(subscriber.publisherValue, value)

    def testPublishSubscribeWithNewStyleConnection(self):
        publisher = Publisher()
        subscriber = Subscriber(2, self.app)
        value = 789
        publisher.updateValue(value)
        self.app.exec_()
        self.assertEqual(subscriber.publisherValue, value)

if __name__ == '__main__':
    unittest.main()

