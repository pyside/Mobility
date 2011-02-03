import unittest

from PySide.QtCore import *
from helper import UsesQApplication
from QtMobility.Feedback import QFeedbackActuator

class QFeedbackActuatorOperatorTest(UsesQApplication):

    def testOperators(self):
        a = QFeedbackActuator()
        b = QFeedbackActuator()
        # When created, QFeedbackActuator instances are initialized with id = -1, so the
        # assert below should work as it uses id for comparison
        self.assert_(a == b)

if __name__ == '__main__':
    unittest.main()


