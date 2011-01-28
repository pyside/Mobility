import os
import unittest
from PySide import QtCore
from QtMobility.SystemInfo import QSystemInfo

class QSystemInfoTest(unittest.TestCase):
    def testSystemInfo(self):
        sysInfo = QSystemInfo()
        self.assertEqual(sysInfo.version(QSystemInfo.Os), os.uname()[2])
        self.assertEqual(sysInfo.version(QSystemInfo.QtCore), QtCore.__version__)

if __name__ == '__main__':
    unittest.main()

