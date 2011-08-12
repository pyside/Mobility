#!/usr/bin/python

import os
import unittest, sys
from PySide.QtCore import QFile, QTimer, QObject, QIODevice, QDateTime, Qt, QDate
from PySide.QtGui import QApplication
from QtMobility.Location import *

from helper import TimedQApplication

def translate_filename(filename):
    'Helper function to prepend the dir of the current file'
    return os.path.join(os.path.dirname(__file__), filename)

class LogFilePositionSource(QGeoPositionInfoSource):
    def __init__(self, parent):
        QGeoPositionInfoSource.__init__(self, parent)
        self.logFile = QFile(self)
        self.timer = QTimer(self)

        self.timer.timeout.connect(self.readNextPosition)

        self.logFile.setFileName(translate_filename('simplelog.txt'))
        assert self.logFile.open(QIODevice.ReadOnly)

        self.lastPosition = QGeoPositionInfo()

    def lastKnownPosition(self, fromSatellitePositioningMethodsOnly):
        return self.lastPosition

    def minimumUpdateInterval(self):
        return 100

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
                    # Currently segfaulting. See Bug 657
                    # http://bugs.openbossa.org/show_bug.cgi?id=657
                    self.positionUpdated.emit(info)


class QtLocationUsage(TimedQApplication):

    def parse_position(self, line):
        timestamp, lat, lng = line.split()

        timestamp = QDateTime.fromString(timestamp, Qt.ISODate)
        lat = float(lat)
        lng = float(lng)

        coordinate = QGeoCoordinate(lat, lng)
        info = QGeoPositionInfo(coordinate, timestamp)

        return info


    def parse_positions(self):
        filename = translate_filename('simplelog.txt')
        with open(filename) as handle:
            return [self.parse_position(line.strip()) for line in handle]

    def setUp(self):
        TimedQApplication.setUp(self, timeout=1000)
        self.expectedPositions = self.parse_positions()
        self.positions = []

    def positionUpdated(self, info):
        self.positions.append(info)

    def testLocation(self):
        source = LogFilePositionSource(self.app)

        source.positionUpdated.connect(self.positionUpdated)
        source.startUpdates()

        self.app.exec_()

        self.assertEqual(self.positions, self.expectedPositions)

if __name__ == '__main__':
    unittest.main()
