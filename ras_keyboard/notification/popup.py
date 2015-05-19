#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class receivedInfo():
	def __init__(self, receivedTime, receivedSender, receivedMsg):
		self.setInfo(receivedTime, receivedSender, receivedMsg)
		
	def setInfo(self, receivedTime, receivedSender, receivedMsg):
		self.time = receivedTime
		self.sender = receivedSender
		self.msg = receivedMsg

class notification(QtGui.QMainWindow):
    def __init__(self, path, info):
        super(notification, self).__init__()
        uic.loadUi('notification.ui', self)
        self.initUI(path, info)
        
    def initUI(self, path, info):
        pixmap = QtGui.QPixmap(path)
        
        self.imgLabel.setPixmap(pixmap.scaled(self.imgLabel.width(), self.imgLabel.height(), QtCore.Qt.KeepAspectRatio))
        self.time.setText(info.time)
        self.sender.setText(info.sender)
        self.contents.setText(info.msg)
        
        self.center()
        self.show()
    
    def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

class MyWindow(QtGui.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        self.kakaotalkBtn = QtGui.QPushButton(self)
        self.kakaotalkBtn.setText("Kakaotalk")
        self.kakaotalkBtn.clicked.connect(self.kakaotalkBtnClicked)

        self.smsBtn = QtGui.QPushButton(self)
        self.smsBtn.setText("SMS")
        self.smsBtn.clicked.connect(self.smsBtnClicked)

        self.layout = QtGui.QHBoxLayout(self)
        self.layout.addWidget(self.kakaotalkBtn)
        self.layout.addWidget(self.smsBtn)
        
        self.resize(300, 250)
        self.center()
        self.setWindowTitle("main window")
        self.show()
    	
    @QtCore.pyqtSlot()
    def kakaotalkBtnClicked(self):
    	path = "image/KAKAOTALK.png"
    	info = receivedInfo("2015/05/13 20:46", "Yanghonam", "example message")
    	self.popup = notification(path, info)
    	self.popup.setWindowTitle("Kakaotalk Notification")
    	
    def smsBtnClicked(self):
    	path = "image/SMS.png"
    	info = receivedInfo("2015/05/28 11:11", "Kim", "example message 2")
    	self.popup = notification(path, info)
    	self.popup.setWindowTitle("SMS Notification")
    	
    def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

def main():
    app = QtGui.QApplication(sys.argv)
    mainWindow = MyWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
