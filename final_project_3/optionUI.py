# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Wed May 20 21:50:57 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from programOption import CSetting

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

global defaultStand

class Ui_Form(object,CSetting):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(63, 83, 78, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox_2 = QtGui.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(163, 83, 78, 27))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_3 = QtGui.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(263, 83, 78, 27))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(153, 243, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit_6 = QtGui.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(143, 163, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(213, 163, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.comboBox_4 = QtGui.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(143, 183, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_5 = QtGui.QComboBox(Form)
        self.comboBox_5.setGeometry(QtCore.QRect(213, 183, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(120, 10, 141, 31))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser_2 = QtGui.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(70, 50, 71, 31))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.textBrowser_3 = QtGui.QTextBrowser(Form)
        self.textBrowser_3.setGeometry(QtCore.QRect(170, 50, 71, 31))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.textBrowser_4 = QtGui.QTextBrowser(Form)
        self.textBrowser_4.setGeometry(QtCore.QRect(260, 50, 71, 31))
        self.textBrowser_4.setObjectName(_fromUtf8("textBrowser_4"))
        self.textBrowser_5 = QtGui.QTextBrowser(Form)
        self.textBrowser_5.setGeometry(QtCore.QRect(130, 130, 141, 31))
        self.textBrowser_5.setObjectName(_fromUtf8("textBrowser_5"))
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.comboBox.setItemText(0, _translate("Form", "0.1", None))
        self.comboBox.setItemText(1, _translate("Form", "0.2", None))
        self.comboBox.setItemText(2, _translate("Form", "0.3", None))
        self.comboBox.setItemText(3, _translate("Form", "0.4", None))
        self.comboBox.setItemText(4, _translate("Form", "0.5", None))
        self.comboBox.setItemText(5, _translate("Form", "0.6", None))
        self.comboBox.setItemText(6, _translate("Form", "0.7", None))
        self.comboBox.setItemText(7, _translate("Form", "0.8", None))
        self.comboBox.setItemText(8, _translate("Form", "0.9", None))
        self.comboBox.setItemText(9, _translate("Form", "1.0", None))
        self.comboBox.setItemText(10, _translate("Form", "1.1", None))
        self.comboBox.setItemText(11, _translate("Form", "1.2", None))
        self.comboBox.setItemText(12, _translate("Form", "1.3", None))
        self.comboBox.setItemText(13, _translate("Form", "1.4", None))
        self.comboBox.setItemText(14, _translate("Form", "1.5", None))
        self.comboBox_2.setItemText(0, _translate("Form", "0.1", None))
        self.comboBox_2.setItemText(1, _translate("Form", "0.2", None))
        self.comboBox_2.setItemText(2, _translate("Form", "0.3", None))
        self.comboBox_2.setItemText(3, _translate("Form", "0.4", None))
        self.comboBox_2.setItemText(4, _translate("Form", "0.5", None))
        self.comboBox_2.setItemText(5, _translate("Form", "0.6", None))
        self.comboBox_2.setItemText(6, _translate("Form", "0.7", None))
        self.comboBox_2.setItemText(7, _translate("Form", "0.8", None))
        self.comboBox_2.setItemText(8, _translate("Form", "0.9", None))
        self.comboBox_2.setItemText(9, _translate("Form", "1.0", None))
        self.comboBox_2.setItemText(10, _translate("Form", "1.1", None))
        self.comboBox_2.setItemText(11, _translate("Form", "1.2", None))
        self.comboBox_2.setItemText(12, _translate("Form", "1.3", None))
        self.comboBox_2.setItemText(13, _translate("Form", "1.4", None))
        self.comboBox_2.setItemText(14, _translate("Form", "1.5", None))
        self.comboBox_3.setItemText(0, _translate("Form", "0.1", None))
        self.comboBox_3.setItemText(1, _translate("Form", "0.2", None))
        self.comboBox_3.setItemText(2, _translate("Form", "0.3", None))
        self.comboBox_3.setItemText(3, _translate("Form", "0.4", None))
        self.comboBox_3.setItemText(4, _translate("Form", "0.5", None))
        self.comboBox_3.setItemText(5, _translate("Form", "0.6", None))
        self.comboBox_3.setItemText(6, _translate("Form", "0.7", None))
        self.comboBox_3.setItemText(7, _translate("Form", "0.8", None))
        self.comboBox_3.setItemText(8, _translate("Form", "0.9", None))
        self.comboBox_3.setItemText(9, _translate("Form", "1.0", None))
        self.comboBox_3.setItemText(10, _translate("Form", "1.1", None))
        self.comboBox_3.setItemText(11, _translate("Form", "1.2", None))
        self.comboBox_3.setItemText(12, _translate("Form", "1.3", None))
        self.comboBox_3.setItemText(13, _translate("Form", "1.4", None))
        self.comboBox_3.setItemText(14, _translate("Form", "1.5", None))
        self.pushButton.setText(_translate("Form", "Setting", None))
        self.lineEdit_6.setText(_translate("Form", "level 2", None))
        self.lineEdit_7.setText(_translate("Form", "level 3", None))
        self.comboBox_4.setItemText(0, _translate("Form", "10", None))
        self.comboBox_4.setItemText(1, _translate("Form", "20", None))
        self.comboBox_4.setItemText(2, _translate("Form", "30", None))
        self.comboBox_4.setItemText(3, _translate("Form", "40", None))
        self.comboBox_4.setItemText(4, _translate("Form", "50", None))
        self.comboBox_4.setItemText(5, _translate("Form", "60", None))
        self.comboBox_4.setItemText(6, _translate("Form", "70", None))
        self.comboBox_4.setItemText(7, _translate("Form", "80", None))
        self.comboBox_4.setItemText(8, _translate("Form", "90", None))
        self.comboBox_4.setItemText(9, _translate("Form", "100", None))
        self.comboBox_5.setItemText(0, _translate("Form", "10", None))
        self.comboBox_5.setItemText(1, _translate("Form", "20", None))
        self.comboBox_5.setItemText(2, _translate("Form", "30", None))
        self.comboBox_5.setItemText(3, _translate("Form", "40", None))
        self.comboBox_5.setItemText(4, _translate("Form", "50", None))
        self.comboBox_5.setItemText(5, _translate("Form", "60", None))
        self.comboBox_5.setItemText(6, _translate("Form", "70", None))
        self.comboBox_5.setItemText(7, _translate("Form", "80", None))
        self.comboBox_5.setItemText(8, _translate("Form", "90", None))
        self.comboBox_5.setItemText(9, _translate("Form", "100", None))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">set weighted value</p></body></html>", None))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Speed</p></body></html>", None))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Steering</p></body></html>", None))
        self.textBrowser_4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">weather</p></body></html>", None))
        self.textBrowser_5.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">set speed standard</p></body></html>", None))
        f = open("input.txt","r")
        defaultStand=[]

        for i in f.readlines():
            defaultStand.append(i)

        self.comboBox.setCurrentIndex(float(defaultStand[0]))
        self.comboBox_2.setCurrentIndex(float(defaultStand[1]))
        self.comboBox_3.setCurrentIndex(float(defaultStand[2]))
        self.comboBox_4.setCurrentIndex(int(defaultStand[3]))
        self.comboBox_5.setCurrentIndex(int(defaultStand[4]))
        f.close()
	
        self.pushButton.clicked.connect(self.setting_button_click)

    def setting_button_click(self):
		CSetting.speedWeightedVal = float(self.comboBox.currentText())
		CSetting.steeringWeightedVal = float(self.comboBox_2.currentText())
		CSetting.weatherWeightedVal = float(self.comboBox_3.currentText())
		CSetting.SpeedStand[1] = int(self.comboBox_4.currentText())
		CSetting.SpeedStand[2] = int(self.comboBox_5.currentText())

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
		


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

