import unittest
from helper import UsesQCoreApplication
from QtMobility.Sensors import QSensorFilter, QSensor

class Filter(QSensorFilter):
    def __init__(self, app):
        QSensorFilter.__init__(self)
        self.app = app
        self.called = False

    def filter(self, reading):
        self.called = True
        self.app.quit()
        return False

class TestSensors(UsesQCoreApplication):
    def setUp(self):
        UsesQCoreApplication.setUp(self)
        self.called = False

    def tearDown(self):
        del self.called
        UsesQCoreApplication.tearDown(self)

    def testFakeSensor(self):
        sensor = QSensor('FakeSensor')
        filt = Filter(self.app)
        sensor.addFilter(filt)
        sensor.start()
        self.assert_(sensor.isActive())
        self.app.exec_()
        self.assert_(filt.called)


if __name__ == '__main__':
    unittest.main()

