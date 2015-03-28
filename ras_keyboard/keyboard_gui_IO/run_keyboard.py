# -*- encoding: utf-8 -*-
# chunjiin keyboard

import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from phone import PhoneAutomata
from joystickRun import *

formClass = uic.loadUiType("chunjiin.ui")[0]    
p = PhoneAutomata(True, debug=False)

class MyWindowClass(QTableWidget, formClass):
    def __init__(self, *args, **kwargs):
        QTableWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
	self.setStyleSheet("background-color: rgb(255, 255, 255);\n"+\
                           "color: rgb(0, 0, 0);\n"+\
                           "border:1px solid #7F462C ;\n")
 
	self.btnOne.clicked.connect(self.btnOne_clicked)
	self.btnTwo.clicked.connect(self.btnTwo_clicked)
	self.btnThree.clicked.connect(self.btnThree_clicked)
        self.btnFour.clicked.connect(self.btnFour_clicked)
	self.btnFive.clicked.connect(self.btnFive_clicked)
	self.btnSix.clicked.connect(self.btnSix_clicked)
	self.btnSeven.clicked.connect(self.btnSeven_clicked)
	self.btnEight.clicked.connect(self.btnEight_clicked)
	self.btnNine.clicked.connect(self.btnNine_clicked)
	self.btnZero.clicked.connect(self.btnZero_clicked)
	print dir
    
    def btnOne_clicked(self):
	self.board('1')

    def btnTwo_clicked(self):
	self.board('2')

    def btnThree_clicked(self):
	self.board('3')

    def btnFour_clicked(self):
	self.board('q')

    def btnFive_clicked(self):
	self.board("w")

    def btnSix_clicked(self):
	self.board("e")

    def btnSeven_clicked(self):
	self.board("a")

    def btnEight_clicked(self):
	self.board("s")

    def btnNine_clicked(self):
	self.board("d")

    def btnZero_clicked(self):
	self.board("x")

    def btnZero_clicked(self):
	self.board("x")

    def board(self, c):
	keypad = {'1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', 				'7':'7', '8':'8', '9':'9', '0':'0',
		  'q':'4', 'w':'5', 'e':'6', 'a':'7', 's':'8', 'd':'9', 		'x':'0'}

	if c == "\x1b" or c == "\x03":
		print "\nbye."
	elif c == " ":
		p.next()
	elif c == "\x7f":
		p.back()
	else:
		if c in keypad:
		    p.feed(keypad[c])
	self.inputText.setText("\r" + p.writer.dump() + " ",)

if __name__ == '__main__':
	app = QtGui.QApplication([])
    	wd = QtGui.QMainWindow()
    	wd.resize(500,400)
    	mb = MyWindowClass()
    	mb.setFixedSize(500,400)
    	wd.setCentralWidget(mb)
    	wd.show()
    	sys.exit(app.exec_())
	app.exec_()
