#!/usr/bin/python

import unittest
from PySide.QtGui import QApplication
from QtMobility.Feedback import *

class QtFeedbackKeyFeature(unittest.TestCase):

    def setUp(self):
        self.wasCalled = False

    def callback(self):
        self.wasCalled = True

    def testFeedbackEffect(self):
        app = QApplication([])

        actuator = QFeedbackActuator()
        actuator.enabledChanged.connect(self.callback)
        actuator.setEnabled(not actuator.isEnabled())

        self.assert_(self.wasCalled)

if __name__ == '__main__':
    unittest.main()
