import unittest

from PySide.QtCore import *
from helper import UsesQCoreApplication

class QFeedbackClassesImportTest(UsesQCoreApplication):

    def testImports(self):
        from QtMobility.Feedback import QFeedbackHapticsInterface, QFeedbackFileInterface

if __name__ == '__main__':
    unittest.main()


