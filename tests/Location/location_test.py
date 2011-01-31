#!/usr/bin/python

import unittest, sys
from PySide.QtCore import QFile, QTimer, QObject, QIODevice, QDateTime, Qt, QDate
from PySide.QtGui import QApplication
from QtMobility.Location import *

class LogFilePositionSource(QGeoPositionInfoSource):
    def __init__(self, parent):
        QGeoPositionInfoSource.__init__(self, parent)
        self.logFile = QFile(self)
        self.timer = QTimer(self)

        self.timer.timeout.connect(self.readNextPosition)

        self.logFile.setFileName("simplelog.txt")
        if not self.logFile.open(QIODevice.ReadOnly):
            print "Error: cannot open source file", self.logFile.fileName()

        self.lastPosition = QGeoPositionInfo()

    def lastKnownPosition(self, fromSatellitePositioningMethodsOnly):
        return self.lastPosition

    def minimumUpdateInterval(self):
        return 500

    def startUpdates(self):
        interval = self.updateInterval()

        if interval < self.minimumUpdateInterval():
            interval = self.minimumUpdateInterval()

        self.timer.start(interval)

    def stopUpdates(self):
        self.timer.stop()

    def requestUpdate(self, timeout):
        # For simplicity, ignore timeout - assume that if data is not available
        # now, no data will be added to the file later
        if (self.logFile.canReadLine()):
            self.readNextPosition()
        else:
            self.updateTimeout.emit()

    def readNextPosition(self):
        line = self.logFile.readLine().trimmed()

        if not line.isEmpty():
            data = line.split(' ')
            hasLatitude = True
            hasLongitude = True
            timestamp = QDateTime.fromString(str(data[0]), Qt.ISODate)
            latitude = float(data[1])
            longitude = float(data[2])
            if timestamp.isValid():
                coordinate = QGeoCoordinate(latitude, longitude)
                info = QGeoPositionInfo(coordinate, timestamp)
                if info.isValid():
                    self.lastPosition = info
                    print "Info:", info
                    self.positionUpdated.emit(info)
        else:
            sys.exit(0)


class QtLocationUsage(unittest.TestCase):

    def positionUpdated(self, info):
        print "Position updated:", info

    def testLocation(self):
        app = QApplication([])
        source = LogFilePositionSource(app)

        if source:
            source.positionUpdated.connect(self.positionUpdated)
            source.startUpdates()

        sys.exit(app.exec_())

if __name__ == '__main__':
    unittest.main()
