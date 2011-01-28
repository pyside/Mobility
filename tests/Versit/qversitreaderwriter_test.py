import unittest
from QtMobility.Versit import *
from PySide.QtCore import *

class QVersitTest(unittest.TestCase):

    def testVersitReaderWriter(self):

        # Read vCard into a QVersitDocument
        bufferIn = QBuffer()
        bufferIn.open(QBuffer.ReadWrite)
        inputVCard = "BEGIN:VCARD\r\nVERSION:2.1\r\nFN:John Constantine\r\nN:Constantine;John;Q;;\r\nEND:VCARD\r\n";
        bufferIn.write(inputVCard)
        bufferIn.seek(0)
        reader = QVersitReader(bufferIn)
        reader.startReading()
        reader.waitForFinished()
        inDocuments = reader.results()
        doc = inDocuments[0]

        # Write a QVersitDocument in vCard format
        bufferOut = QBuffer()
        bufferOut.open(QBuffer.ReadWrite)
        writer = QVersitWriter()
        writer.setDevice(bufferOut)
        writer.startWriting(doc)
        writer.waitForFinished()
        
        #Verify if the vCard survived the trip
        self.assertEquals(bufferOut.buffer(), inputVCard)

if __name__ == '__main__':
    unittest.main()
