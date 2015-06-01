# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Tue May 19 22:53:55 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import DataStore

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(0, 110, 78, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox_2 = QtGui.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(100, 110, 78, 27))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
	self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_3 = QtGui.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(200, 110, 78, 27))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
	self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(0, 80, 81, 31))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 80, 81, 31))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 80, 81, 31))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(90, 180, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

	self.label = QtGui.QLabel(Form)
	self.label.setGeometry(QtCore.QRect(0, 10, 100, 30))
	self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.comboBox.setItemText(0, _translate("Form", "0.8", None))
        self.comboBox.setItemText(1, _translate("Form", "0.9", None))
        self.comboBox.setItemText(2, _translate("Form", "1.0", None))
        self.comboBox.setItemText(3, _translate("Form", "1.1", None))
        self.comboBox.setItemText(4, _translate("Form", "1.2", None))
        self.comboBox_2.setItemText(0, _translate("Form", "0.8", None))
        self.comboBox_2.setItemText(1, _translate("Form", "0.9", None))
        self.comboBox_2.setItemText(2, _translate("Form", "1.0", None))
	self.comboBox_2.setItemText(3, _translate("Form", "1.1", None))
	self.comboBox_2.setItemText(4, _translate("Form", "1.2", None))
        self.comboBox_3.setItemText(0, _translate("Form", "0.8", None))
        self.comboBox_3.setItemText(1, _translate("Form", "0.9", None))
        self.comboBox_3.setItemText(2, _translate("Form", "1.0", None))	
	self.comboBox_3.setItemText(3, _translate("Form", "1.1", None))
	self.comboBox_3.setItemText(4, _translate("Form", "1.2", None))
        self.lineEdit.setText(_translate("Form", "speed", None))
        self.lineEdit_2.setText(_translate("Form", "steering", None))
        self.lineEdit_3.setText(_translate("Form", "weather", None))
        self.pushButton.setText(_translate("Form", "Setting", None))

	self.label.setText(_translate("Form", "test", None))
    	self.pushButton.clicked.connect(self.setting_button_click)

    def setting_button_click(self):
        DataStore.speedWeightedVal = int(self.comboBox.currentText())
        DataStore.steeringWeightedVal = int(self.comboBox_2.currentText())
        DataStore.weatherWeightedVal = int(self.comboBox_3.currentText())


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

