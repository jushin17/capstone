# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Wed May 20 10:47:58 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import DataStore
from setting import CSetting
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

formClass = uic.loadUiType("test.ui")[0]  

class Ui_Form(QTableWidget, formClass):
    def __init__(self, *args, **kwargs):
        QTableWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setStyleSheet("background-color: rgb(255, 255, 255);\n"+\
                           "color: rgb(0, 0, 0);\n"+\
                           "border:1px solid #7F462C ;\n")
        self.pushButton.clicked.connect(self.setting_button_click)

    def setting_button_click(self):
		setting.CSetting.speedWeightedVal = int(self.comboBox.currentText())
		setting.CSetting.steeringWeightedVal = int(self.comboBox_2.currentText())
		setting.CSetting.weatherWeightedVal = int(self.comboBox_3.currentText())
		setting.CSetting.SpeedStand[1] = int(self.comboBox_4.currentText())
		setting.CSetting.SpeedStand[2] = int(self.comboBox_5.currentText())
		self.label.setText(str(self.comboBox.currentText()))
		#print "speedWeightedVal:"
		#print setting.CSetting.speedWeightedVal
		#print "steeringWeightedVal:"
		#print setting.CSetting.steeringWeightedVal
		#print "weatherWeightedVal:"
		#print setting.CSetting.weatherWeightedVal
		#print "SpeedStandard 1 : "
		#print setting.CSetting.SpeedStand[1]
		#print "SpeedStandard 2 : "
		#print setting.CSetting.SpeedStand[2]
		self.close()


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	Form = QtGui.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())

