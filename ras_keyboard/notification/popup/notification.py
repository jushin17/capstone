#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import threading
import time
from PyQt4 import QtCore, QtGui, uic
from audioplay import *

class notification(QtGui.QMainWindow):
    def __init__(self, level):
        super(notification, self).__init__()
        uic.loadUi('notification.ui', self)
        self.initUI(level)
        
    def initUI(self, level):
    	warningMsg = "Level is " + str(level) + "." + '\n'
    	if level == 2:
    		warningMsg += "Input is restricted."
    	elif level == 3:
    		warningMsg += "Input and notify are restricted."
    	else:
    		warningMsg += "You can input and be notified."
        
        self.warningText.setText(warningMsg)
        
        self.center()
        self.show()
        #self.showFullScreen()
    
    def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

def popup(level):
	app = QtGui.QApplication(sys.argv)
	popupWindow = notification(level)
	print("before")
	app.exec_()
	print("after")

def notify(level):
	th1 = threading.Thread(target=popup, args=(level,))
	th1.start()
	if level == 2:
		audiofile = "audio.wav"
	elif level == 3:
		audiofile = "audio.wav"
	else:
		audiofile = "audio2.wav"
	th2 = threading.Thread(target=audioplay, args=(audiofile,))
	th2.start()

def main():
	notify(2)

if __name__ == '__main__':
    main()
