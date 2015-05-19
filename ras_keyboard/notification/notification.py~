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

def popup(path, time, name, msg):
	app = QtGui.QApplication(sys.argv)
	info = receivedInfo(time, name, msg)
	noti = notification(path, info)
	sys.exit(app.exec_())

def main():
    popup("image/KAKAOTALK.png", "2015/05/18 16:32", "Yanghonam", "hello")

if __name__ == '__main__':
    main()
