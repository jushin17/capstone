#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui

class MyWindow(QtGui.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        
        self.newWindowButton = QtGui.QPushButton(self)
        self.newWindowButton.setText("New Window")
        self.newWindowButton.clicked.connect(self.newWindowButtonClicked)

        self.quitButton = QtGui.QPushButton(self)
        self.quitButton.setText("Quit")
        self.quitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.layout = QtGui.QHBoxLayout(self)
        self.layout.addWidget(self.newWindowButton)
        self.layout.addWidget(self.quitButton)
        
        self.resize(300, 250)
        self.setWindowTitle("MyWindow")
        self.show()
    	
    @QtCore.pyqtSlot()
    def newWindowButtonClicked(self):
    	self.newWindow = MyWindow()

def main():
    app = QtGui.QApplication(sys.argv)
    myWindow = MyWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
