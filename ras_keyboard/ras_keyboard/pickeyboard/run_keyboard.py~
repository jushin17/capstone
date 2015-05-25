import sys
import os
import utils
import time

from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class SlideShowPics(QtGui.QMainWindow):

	# SlideShowPics class defines the methods for UI and working logic
	def __init__(self, parent=None):
		super(SlideShowPics, self).__init__(parent)
		# self._path = path	
		self.stC = 0 #stC=0 -> consonant, st=1 -> backspace, esc key	
		self.stV = 0 #stV=0 -> vowel, stV=1 -> number
		self.mFlagC = True #different main screen(consonant, each things)
		self.mFlagV = False #different main screen(vowel, each things)
		
		self.prepairWindow()
		self.buildUi()
		self.changeImgC() #change consonant, backspace, esc
		self.changeImgV() #change vowel, number
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		
	def prepairWindow(self):
		# Centre UI	
		screen = QtGui.QDesktopWidget().screenGeometry(self)
		size = self.geometry()

		self.centralWidget 	=  QWidget(self)
		self.layout 		=  QGridLayout()	
		self.verticalLine 	=  QFrame()
		self.centralWidget.setLayout(self.layout)
		self.verticalLine.setFrameStyle(QFrame.VLine)
		self.verticalLine.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Expanding)
		self.setStyleSheet("QWidget{background-color:WHITE;}")
		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint) #the main window will stay always on top of the other apps.
		self.splash=QtGui.QLabel()
		self.splash.setAlignment(QtCore.Qt.AlignCenter)
		self.showMaximized()
		#self.showFullScreen()
		#self.setFixedSize(screen.width(), screen.height())
		
		self.buildUi()

	def buildUi(self):
		font = QtGui.QFont("UnDotum",30,QtGui.QFont.Bold,False)
		
		self.le = QLineEdit()
		self.le.setObjectName("inputText")
		self.le.setReadOnly(False)
		self.le.setFont(font)
		self.le.setTextMargins (15, 15, 15, 15)
		self.connect(self.le, SIGNAL("returnPressed()"), self.update)
		self.setMenuWidget(self.le)

		self.label = QtGui.QLabel() #create left label
		self.label.setAlignment(QtCore.Qt.AlignLeft)	
		
		self.label2 = QtGui.QLabel() #create right label
		self.label2.setAlignment(QtCore.Qt.AlignRight)
		
		self.layout.addWidget(self.label,0,0)
		self.layout.addWidget(self.label2,0,1)

		self.setCentralWidget(self.centralWidget)

	def changeImgC(self):
		# switch to main image(consonant or vowel) or second image(detail)
		if self.stC == 0:
			self.mFlagC=True
			self.showImageByPathC(
					'image/consonant/8basis.png')

		elif self.stC == 1:
			self.mFlagC=True
			self.showImageByPathC(
					'image/consonant/esc.png')

	def changeImgV(self):
		if self.stV == 0:
			self.mFlagV=True
			self.showImageByPathV(
					'image/vowel/8basis.png')

		elif self.stV == 1:
			self.mFlagC=True
			self.showImageByPathV(
					'image/vowel/udlr.png')

	def showImageByPathC(self, path):
		image = QtGui.QImage(path)
		pp = QtGui.QPixmap.fromImage(image)
		self.label.setPixmap(pp.scaled(
				self.label.size(),
				QtCore.Qt.KeepAspectRatio,
				QtCore.Qt.SmoothTransformation))

	def showImageByPathV(self, path):
		image2 = QtGui.QImage(path)
		pp2 = QtGui.QPixmap.fromImage(image2)
		self.label2.setPixmap(pp2.scaled(
				self.label2.size(),
				QtCore.Qt.KeepAspectRatio,
				QtCore.Qt.SmoothTransformation))
	
	def update(self):
		self.le.clear()
		
	def eventCos(self, event):
		if event == QtCore.Qt.Key_Escape:
			self.close()

		elif self.mFlagC==True and event == QtCore.Qt.Key_Q:
			self.mFlagC=False
			if self.stC == 0:
				self.showImageByPathC('image/consonant/8arrow.png')

		elif self.mFlagC==True and event == QtCore.Qt.Key_W:
			self.mFlagC=False
			if self.stC == 0:
				self.showImageByPathC('image/consonant/1arrow.png')

		elif self.mFlagC==True and event == QtCore.Qt.Key_E:
			self.mFlagC=False
			if self.stC == 0:
				self.showImageByPathC('image/consonant/2arrow.png')

		elif self.mFlagC==True and event == QtCore.Qt.Key_A:
			self.mFlagC=False
			if self.stC == 0:
				self.stC = 1
				self.changeImgC()

		elif self.mFlagC==True and event == QtCore.Qt.Key_D:
			self.mFlagC=False
			if self.stC == 0:
				self.showImageByPathC('image/consonant/3arrow.png')

		elif self.mFlagC==True and event == QtCore.Qt.Key_Z:
			self.mFlagC=False
			if self.stC == 0:
				self.showImageByPathC('image/consonant/6arrow.png')

		elif self.mFlagC==True and event == QtCore.Qt.Key_X:
			self.mFlagC=False
			if self.stC == 0:
				self.showImageByPathC('image/consonant/5arrow.png')
			elif self.stC == 1: 
				self.stC = 0
				self.changeImgC()

		elif self.mFlagC==True and event == QtCore.Qt.Key_C:
			self.mFlagC=False
			if self.stC == 0:
				self.showImageByPathC('image/consonant/4arrow.png')

		elif self.mFlagC==True and event == QtCore.Qt.Key_S: 
			#this state-main screen and click down
			if self.stC == 0:
				print "CLICK"

		elif self.mFlagC==True and event == QtCore.Qt.Key_Enter: 
			#this state-main screen and click down
			if self.stC == 0:
				self.le.clear()
				
		elif self.mFlagC==False:
			if self.stC == 0:
				if event == QtCore.Qt.Key_Q or event == QtCore.Qt.Key_W or event == QtCore.Qt.Key_E or event == QtCore.Qt.Key_A or  event == QtCore.Qt.Key_D or event == QtCore.Qt.Key_Z or event == QtCore.Qt.Key_X or event == QtCore.Qt.Key_C: #change main screen after insert Nothing
					self.changeImgC()
			elif self.stC == 1:				
				if event == QtCore.Qt.Key_X:
					self.stC = 0
					self.changeImgC()
			
	def eventVow(self, event):
		if self.mFlagV==True and event == QtCore.Qt.Key_T:
			self.mFlagV=False
			if self.stV == 0:
				self.showImageByPathV('image/vowel/8arrow.png')

		elif self.mFlagV==True and event == QtCore.Qt.Key_Y:
			self.mFlagV=False
			if self.stV == 0:
				self.showImageByPathV('image/vowel/1arrow.png')

		elif self.mFlagV==True and event == QtCore.Qt.Key_U:
			self.mFlagV=False
			if self.stV == 0:
				self.showImageByPathV('image/vowel/2arrow.png')

		elif self.mFlagV==True and event == QtCore.Qt.Key_G:
			self.mFlagV=False
			if self.stV == 0:
				self.showImageByPathV('image/vowel/7arrow.png')

		elif self.mFlagV==True and event == QtCore.Qt.Key_J:
			self.mFlagV=False
			if self.stV == 0:
				self.showImageByPathV('image/vowel/3arrow.png')

		elif self.mFlagV==True and event == QtCore.Qt.Key_B:
			self.mFlagV=False
			if self.stV == 0:
				self.showImageByPathV('image/vowel/6arrow.png')

		elif self.mFlagV==True and event == QtCore.Qt.Key_M:
			self.mFlagV=False
			if self.stV == 0:
				self.showImageByPathV('image/vowel/4arrow.png')

		elif self.mFlagV==True and event == QtCore.Qt.Key_H:
			self.mFlagV=False
			if self.stV == 0:
				self.stV = 1
				self.changeImgV()

		elif self.mFlagV==False:
			if self.stV == 0:		
				if event == QtCore.Qt.Key_N or event == QtCore.Qt.Key_G or event == QtCore.Qt.Key_Y or event == QtCore.Qt.Key_J:	#change main screen after insert
					self.changeImgV()
			elif self.stV == 1:
				if event == QtCore.Qt.Key_H:
					self.stV = 0
					self.changeImgV()

	def keyPressEvent(self, keyevent):
		# Capture key to exit, next image, previous image, on Escape , Key Right and key left respectively.
		self.event = keyevent.key()
		self.eventCos(self.event)
		self.eventVow(self.event)

def main():
	app = QtGui.QApplication(sys.argv)
	window = SlideShowPics()

	# Create and display the splash screen
	splash_pix = QPixmap('image/splash.jpg')
	splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
	splash.setMask(splash_pix.mask())
	splash.show()
	app.processEvents()

    # Simulate something that takes time
	splash.finish(window)
	window.show()
	window.raise_()
	app.exec_()

if __name__ == '__main__':
	main()
