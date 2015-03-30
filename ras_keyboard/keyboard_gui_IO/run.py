# -*- encoding: utf-8 -*-
# chunjiin keyboard

import sys
from PyQt4 import QtCore, QtGui, uic
from getch import _Getch
from phone import PhoneAutomata

form_class = uic.loadUiType("chunjiin.ui")[0]    
p = PhoneAutomata(True, debug=False)

class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
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
	
    def btnOne_clicked(self):
	self.keyboard('1')

    def btnTwo_clicked(self):
	self.keyboard('2')

    def btnThree_clicked(self):
	self.keyboard('3')

    def btnFour_clicked(self):
	self.keyboard('q')

    def btnFive_clicked(self):
	self.keyboard("w")

    def btnSix_clicked(self):
	self.keyboard("e")

    def btnSeven_clicked(self):
	self.keyboard("a")

    def btnEight_clicked(self):
	self.keyboard("s")

    def btnNine_clicked(self):
	self.keyboard("d")

    def btnZero_clicked(self):
	self.keyboard("x")

    def keyboard(self, c):

	keypad = {'1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', 				'7':'7', '8':'8', '9':'9', '0':'0',
		  'q':'4', 'w':'5', 'e':'6', 'a':'7', 's':'8', 'd':'9', 		'x':'0'}

	getch = _Getch()
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


app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass(None)
myWindow.show()
app.exec_()
