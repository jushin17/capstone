#-*- coding:utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class notification(QtGui.QMainWindow):
    def __init__(self):
        super(notification, self).__init__()
        uic.loadUi('notification.ui', self)
        self.initUI()
        
    def initUI(self):
        pixmap = QtGui.QPixmap("/home/parallels/Desktop/notification/KAKAOTALK.png")
        
        self.imgLabel.setPixmap(pixmap.scaled(self.imgLabel.width(), self.imgLabel.height(), QtCore.Qt.KeepAspectRatio))
        
        self.move(300, 200)
        self.setWindowTitle("Notification")
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    window = notification()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
