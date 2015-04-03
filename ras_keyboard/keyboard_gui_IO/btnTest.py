import sys
from PyQt4 import QtGui, QtCore
from run import MyWindowClass

class QCustomWidget (QtGui.QWidget):
    def __init__ (self, parent = None):
        super(QCustomWidget, self).__init__(parent)
        myQLayout = QtGui.QVBoxLayout()
        self.my1QPushButton = QtGui.QPushButton('Test 1', self)
        self.my2QPushButton = QtGui.QPushButton('Test 2', self)
        myQLayout.addWidget(self.my1QPushButton)
        myQLayout.addWidget(self.my2QPushButton)
        self.my1QPushButton.keyPressEvent = self.button1KeyPressEvent
        self.my2QPushButton.keyPressEvent = self.button2KeyPressEvent
        self.setLayout(myQLayout)

    def keyPressEvent (self, eventQKeyEvent):
        messageQMessageBox = QtGui.QMessageBox(QtGui.QMessageBox.Question, 'Question', 'Hello Main', QtGui.QMessageBox.Yes)
        messageQMessageBox.exec_()
        QtGui.QWidget.keyPressEvent(self, eventQKeyEvent)

    def button1KeyPressEvent (self, eventQKeyEvent):
        messageQMessageBox = QtGui.QMessageBox(QtGui.QMessageBox.Question, 'Question', 'Hello Button 1', QtGui.QMessageBox.Yes)
        messageQMessageBox.exec_()
        QtGui.QPushButton.keyPressEvent(self.my1QPushButton, eventQKeyEvent)

    def button2KeyPressEvent (self, eventQKeyEvent):
        messageQMessageBox = QtGui.QMessageBox(QtGui.QMessageBox.Question, 'Question', 'Hello Button 2', QtGui.QMessageBox.Yes)
        messageQMessageBox.exec_()
        QtGui.QPushButton.keyPressEvent(self.my2QPushButton, eventQKeyEvent)

appQApplication = QtGui.QApplication(sys.argv)
windowQCustomWidget = QCustomWidget()
windowQCustomWidget.setFixedSize(640, 480)
windowQCustomWidget.show()
sys.exit(appQApplication.exec_())
