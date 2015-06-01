# -*- coding: utf-8 -*-
import sys
import matplotlib as mpl
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from programOption import CSetting


formClass = uic.loadUiType("test.ui")[0]

global defaultStand

class Ui_Form(QWidget, formClass, CSetting):
	def __init__(self):
		QWidget.__init__(self)
		self.setupUi(self)
		f = open("input.txt","r")
		defaultStand=[]
		
		for i in f.readlines():
			defaultStand.append(i)

		self.setFocusPolicy(QtCore.Qt.TabFocus)
		

		self.comboBox.setCurrentIndex(float(defaultStand[0]))
		self.comboBox_2.setCurrentIndex(float(defaultStand[1]))
		self.comboBox_3.setCurrentIndex(float(defaultStand[2]))
		self.comboBox_4.setCurrentIndex(int(defaultStand[3]))
		self.comboBox_5.setCurrentIndex(int(defaultStand[4]))
		f.close()
		
		self.pushButton.clicked.connect(self.setting_button_click)

	def complete(self):
		QtCore.QCoreApplication.instance().quit()

	def setting_button_click(self):
		print "speedWeightedVal:"
		print CSetting.speedWeightedVal
		print "steeringWeightedVal:"
		print CSetting.steeringWeightedVal
		print "weatherWeightedVal:"
		print CSetting.weatherWeightedVal
		print "SpeedStandard 1 : "
		print CSetting.SpeedStand[1]
		print "SpeedStandard 2 : "
		print CSetting.SpeedStand[2]
		print self.comboBox.currentIndex()
		CSetting.speedWeightedVal = float(self.comboBox.currentText())
		CSetting.steeringWeightedVal = float(self.comboBox_2.currentText())
		CSetting.weatherWeightedVal = float(self.comboBox_3.currentText())
		CSetting.SpeedStand[1] = int(self.comboBox_4.currentText())
		CSetting.SpeedStand[2] = int(self.comboBox_5.currentText())

		print "speedWeightedVal:"
		print CSetting.speedWeightedVal
		print "steeringWeightedVal:"
		print CSetting.steeringWeightedVal
		print "weatherWeightedVal:"
		print CSetting.weatherWeightedVal
		print "SpeedStandard 1 : "
		print CSetting.SpeedStand[1]
		print "SpeedStandard 2 : "
		print CSetting.SpeedStand[2]
		print self.comboBox.currentIndex()
		f = open("input.txt","w")
		f.write(str(self.comboBox.currentIndex()))
		f.write("\n")
		f.write(str(self.comboBox_2.currentIndex()))
		f.write("\n")
		f.write(str(self.comboBox_3.currentIndex()))
		f.write("\n")
		f.write(str(self.comboBox_4.currentIndex()))
		f.write("\n")
		f.write(str(self.comboBox_5.currentIndex()))
		f.write("\n")
		f.close()
		QtCore.QCoreApplication.instance().quit()

	def keyPressEvent(self, e):
		if e.key() == QtCore.Qt.Key_Return:
			self.setting_button_click()
			QtCore.QCoreApplication.instance().quit()
		else:
			e.accept()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QMainWindow()
    Form.resize(400, 300)
    ui = Ui_Form()
    Form.setCentralWidget(ui)
    Form.show()
    sys.exit(app.exec_())
