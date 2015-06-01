# -*- coding: UTF-8 -*-

import sys
import os
import utils
import uinput
import spidev
import time
#from time import time
import threading
import PiTooth
import obdMain
import audioplay
import optionUI
import thread
from DataStore import CDataStore

#import matplotlib as mpl

from PyQt4 import QtGui,QtCore, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from programOption import CSetting

device = uinput.Device([uinput.KEY_A,
			uinput.KEY_B,
			uinput.KEY_C,
			uinput.KEY_D,
			uinput.KEY_E,
			uinput.KEY_F,
			uinput.KEY_G,
			uinput.KEY_H,
			uinput.KEY_I,
			uinput.KEY_J,
			uinput.KEY_K,
			uinput.KEY_L,
			uinput.KEY_M,
			uinput.KEY_N,
			uinput.KEY_O,
			uinput.KEY_P,
			uinput.KEY_Q,
			uinput.KEY_R,
			uinput.KEY_S,
			uinput.KEY_T,
			uinput.KEY_U,
			uinput.KEY_V,
			uinput.KEY_W,
			uinput.KEY_X,
			uinput.KEY_Y,
			uinput.KEY_Z,
			uinput.KEY_LEFTSHIFT,
			uinput.KEY_ENTER,
			uinput.KEY_SPACE,
			uinput.KEY_BACKSPACE,
			uinput.KEY_UP,
			uinput.KEY_DOWN,
			uinput.KEY_LEFT,
			uinput.KEY_RIGHT,
			uinput.KEY_TAB
			])

functionmap = [[device.emit_click, device.emit_combo, False, device.emit_click],  #€¡, €¢, €»
               [device.emit_click, device.emit_click, False, device.emit_click],  #    €€, €©
               [device.emit_click, device.emit_combo, False, device.emit_click],  #€§, €š, €Œ
               [device.emit_click, device.emit_combo, False, device.emit_click],  #€², €³, €œ
               [device.emit_click, device.emit_combo, False, device.emit_click],  #¶çŸîŸ²±â
               [device.emit_click, device.emit_combo, False, device.emit_click],  #   €¶, €µ
               [False, device.emit_click, False, device.emit_click],
               [device.emit_click, device.emit_click, False, device.emit_click]]  #€·, €Ÿ, €±

parmmap = [[uinput.KEY_R, [uinput.KEY_LEFTSHIFT, uinput.KEY_R], False, uinput.KEY_Z],
           [uinput.KEY_S, uinput.KEY_F, []],
           [uinput.KEY_E, [uinput.KEY_LEFTSHIFT, uinput.KEY_E], False, uinput.KEY_X],
           [uinput.KEY_Q, [uinput.KEY_LEFTSHIFT, uinput.KEY_Q], False, uinput.KEY_V],
           [uinput.KEY_W, [uinput.KEY_LEFTSHIFT, uinput.KEY_W], False, uinput.KEY_C],
           [uinput.KEY_T, [uinput.KEY_LEFTSHIFT, uinput.KEY_T], False, []],
           [False, uinput.KEY_ESC, False, uinput.KEY_BACKSPACE],
           [uinput.KEY_D, uinput.KEY_G, False, uinput.KEY_A]]

bluemap = [[[True, "KEY_R"],[False, "KEY_R"],[],[True, "KEY_Z"]],   #True = one, False = two
[[True, "KEY_S"],[True, "KEY_F"],[],[]],
[[True, "KEY_E"],[False, "KEY_E"],[],[True, "KEY_X"]],
[[True, "KEY_Q"],[False, "KEY_Q"],[],[True, "KEY_V"]],
[[True, "KEY_W"],[False, "KEY_W"],[],[True, "KEY_C"]],
[[True, "KEY_T"],[False, "KEY_T"],[],[]],
[[],[True, "KEY_ESC"],[],[True, "KEY_BACKSPACE"]],
[[True, "KEY_D"],[True, "KEY_G"],[],[True, "KEY_A"]]]



ismap1 = [[True, True, False, True],
         [True, True, False, False],
         [True, True, False, True],
         [True, True, False, True],
         [True, True, False, True],
         [True, True, False, False],
         [True, True, True, True],
         [True, True, False, True]]

audiomap = [[[True, "r.wav"], [True, "rr.wav"], [False], [True, "z.wav"]],
         [[True, "s.wav"], [True, "f.wav"], [False], [False]],
         [[True, "e.wav"], [True, "ee.wav"], [False], [True, "x.wav"]],
         [[True, "q.wav"], [True, "qq.wav"], [False], [True, "v.wav"]],
         [[True, "w.wav"], [True, "ww.wav"], [False], [True, "c.wav"]],
         [[True, "t.wav"], [True, "tt.wav"], [False], [False]],
         [[False], [False], [False], [False]],
         [[True, "d.wav"], [True, "g.wav"], [False], [True, "a.wav"]]]

functionmap2 = [[device.emit_click, device.emit_click, False, device.emit_click],  #€¡, €¢, €»
               [device.emit_click, device.emit_combo, False, device.emit_click],  #    €€, €©
               [device.emit_click, device.emit_click, False, device.emit_click],  #€§, €š, €Œ
               [device.emit_click, device.emit_click, False, device.emit_click],  #€², €³, €œ
               [device.emit_click, device.emit_click, False, device.emit_click],  #¶çŸîŸ²±â
               [device.emit_click, device.emit_click, False, device.emit_click],  #   €¶, €µ
               [device.emit_click, device.emit_click, False, device.emit_click],  #€ž, €¹, €º
               [device.emit_click, device.emit_combo, False, device.emit_click]]  #€·, €Ÿ, €±

parmmap2 = [[[], uinput.KEY_Y, False, uinput.KEY_H],
           [[], [uinput.KEY_LEFTSHIFT, uinput.KEY_O], False, uinput.KEY_O],
           [[], uinput.KEY_I, False, uinput.KEY_K],
           [[], uinput.KEY_B, False, uinput.KEY_N],
           [uinput.KEY_SPACE, uinput.KEY_SPACE, False, uinput.KEY_SPACE],
           [[], uinput.KEY_L, False, uinput.KEY_M],
           [[], uinput.KEY_U, False, uinput.KEY_J],
           [[], [uinput.KEY_LEFTSHIFT, uinput.KEY_P], False, uinput.KEY_P]]

ismap2 = [[False, True, False, True],
         [False, True, False, True],
         [False, True, False, True],
         [False, True, False, True],
         [True, True, False, True],
         [False, True, False, True],
         [False, True, False, True],
         [False, True, False, True]]

bluemap2 = [
[[],[True, "KEY_Y"],[],[True, "KEY_H"]],
[[],[False, "KEY_O"],[],[True, "KEY_O"]],
[[],[True, "KEY_I"],[],[True, "KEY_K"]],
[[],[True, "KEY_B"],[],[True, "KEY_N"]],
[[True, "KEY_SPACE"],[True, "KEY_SPACE"],[],[True, "KEY_SPACE"]],
[[],[True, "KEY_L"],[],[True, "KEY_M"]],
[[],[True, "KEY_U"],[],[True, "KEY_J"]],
[[],[False, "KEY_P"],[],[True, "KEY_P"]]]


audiomap2 = [[[False], [True, "y.wav"], [False], [True, "h.wav"]],
         [[False], [True, "oo.wav"], [False], [True, "o.wav"]],
         [[False], [True, "i.wav"], [False], [True, "k.wav"]],
         [[False], [True, "b.wav"], [False], [True, "n.wav"]],
         [[False], [False], [False], [False]],
         [[False], [True, "l.wav"], [False], [True, "m.wav"]],
         [[False], [True, "u.wav"], [False], [True, "j.wav"]],
         [[False], [True, "pp.wav"], [False], [True, "p.wav"]]]

window = None
Form = None
app = None


bt = None
kb = None


# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)		# it will open /dev/spidev-0.0
 

busInput=[0,0,0,0,0,0]
busState=[0,0,0,0,0,0]
busClose=False

def SpiChannelLoop():
	global busInput
	global busState
	global busClose
	print "Initialize SpiChannelLoop"
	while not busClose:
		for channel in range(6):
			adc = spi.xfer2([1,(8+channel)<<4,0])
			busInput[channel] = ((adc[1]&3)<<8) + adc[2]
			busState[channel] = True
		time.sleep(0.05)
	print "Exit SpiChannelLoop"

# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
	global busInput
	global busState
	global busClose
	#adc = spi.xfer2([1,(8+channel)<<4,0])
	#data = ((adc[1]&3) << 8) + adc[2]
	while not busState[channel]:
		pass
	return busInput[channel]

delay = 0.1

joy_xL=1
joy_yL=2
joy_buttonL=0

joy_xR=4
joy_yR=5
joy_buttonR=3

state = 0
R_pase = 0

position_R = -1

lock = thread.allocate_lock()

OptionState = True

cqueue = []

def keyboard():
	print "start keyboard1"
	global window
	global bt
	global kb
	global state
	global monitoroff
	global OptionState

	monitoroff = False
	isOneclick = False
	isSelect = False
	state = 0
	pase = 0
	x_s = -1
	y_s = -1

	position = -1

	pos_75d = False
	pos_15d = False
	pos_165d = False
	pos_105d = False

	pos_45d = False
	pos_135d = False

	OptionState = True

	while True:
		xPos=ReadChannel(joy_xL) - 512
		yPos=ReadChannel(joy_yL) - 512
  
		pos_45d = False
		pos_135d = False
	
		if isSelect == True:
			isSelect = False
			if x_s < 0:
				pass
			else:
				if x_s == 1:
					device.emit_click(uinput.KEY_TAB)
					x_s = -1

		if xPos <= yPos:
			pos_45d = True
		if (-1)*xPos <= yPos:
			pos_135d = True
		if xPos*xPos + yPos*yPos <= 256*256:
			position = -1
		elif pos_45d == False and pos_135d == True:
			position = 1
		else:
			position = 2

		x_s = -1
		if position == -1: #no move
			isOneclick = False;
		elif position == 1:
			if isOneclick == False:
				isOneclick = True
				x_s = position
				isSelect = True
		else:
			pass

		if OptionState == False and position == -1:
			break

	monitoroff = False
	isOneclick = False
	isSelect = False
	state = 0
	pase = 0
	x_s = -1
	y_s = -1

	position = -1

	pos_75d = False
	pos_15d = False
	pos_165d = False
	pos_105d = False

	pos_45d = False
	pos_135d = False

	print "keyboardL next"

	while not window:
		time.sleep(0.1)

	while True:
                xPos=ReadChannel(joy_xL) - 512
                yPos=ReadChannel(joy_yL) - 512
        
                pos_75d = False  #1
                pos_15d = False  #2
                pos_165d = False  #3
                pos_105d = False  #4
                pos_45d = False
                pos_135d = False
            
                if isSelect == True:
        		isSelect = False
                        if x_s < 0 or y_s < 0:
        			pass
                        else:
        			if ismap1[x_s][y_s] == True:
                                        if CDataStore.Level == 2:
                                                lock.acquire()
                                                audioplay.audioplay("lv2.wav", 44100)
        					lock.release()
        					window.stC = 0  #cons
                                                window.mFlagC = False
                                                #window.eventCos(-1)
                                                state = 0
                                                x_s = -1
                                                y_s = -1
                                        elif CDataStore.Level == 3:
                                                lock.acquire()
        					audioplay.audioplay("lv3.wav", 44100)
        					lock.release()
        					window.stC = 0  #cons
                                                window.mFlagC = False
                                                #window.eventCos(-1)
                                                state = 0
                                                x_s = -1
                                                y_s = -1
                                                #window.eventCos(-2)
                                        elif x_s == 6 and y_s == 0:
        					window.eventCos(-2)
                                                window.monitoroff = True
                                                state = 0
                                                x_s = -1
                                                y_s = -1
                                        elif x_s == 6 and y_s == 2:
        					window.monitoroff = False
                                                state = 0
                                                x_s = -1
                                                y_s = -1
                                        else:
        					functionmap[x_s][y_s](parmmap[x_s][y_s])
                                                if audiomap[x_s][y_s][0] == True:
                                                        lock.acquire()
        						audioplay.audioplay(audiomap[x_s][y_s][1])
        						lock.release()
                                                if bluemap[x_s][y_s][0] == True:
        						#pass
							kb.send_event(bluemap[x_s][y_s][1], 1, bt)
							kb.send_event(bluemap[x_s][y_s][1], 0, bt)							
                                                else:
        						#pass
							kb.send_event("KEY_LEFTSHIFT", 1, bt)
							kb.send_event(bluemap[x_s][y_s][1], 1, bt)
							kb.send_event(bluemap[x_s][y_s][1], 0, bt)
							kb.send_event("KEY_LEFTSHIFT", 0, bt)        
                                                if x_s == 6:
        						y_s = -1
                                                else:							
        						window.stC = 0  #cons
                                                        window.mFlagC = False
                                                        window.eventCos(-1)
                                                        state = 0
                                                        x_s = -1
                                                        y_s = -1
                if state == 0:
        		if 3.732*xPos <= yPos: #80d = 5.671 , 75d = 3.732
                                pos_75d = True
                        if 0.268*xPos <= yPos: #10d = 0.176 , 15d = 0.268
        			pos_15d = True
                        if -0.268*xPos <= yPos: #170d = -0.176 , 165d = -0.268
        			pos_165d = True
                        if -3.732*xPos <= yPos: #100d = -5.671 , 105d = -3.732
        			pos_105d = True        
                        if xPos*xPos + yPos*yPos <= 256*256:
        			position = -1
                        elif pos_75d == True and pos_15d == True and pos_165d == True and pos_105d == True:
        			position = 0
                        elif pos_75d == False and pos_15d == True and pos_165d == True and pos_105d == True:
        			position = 1
                        elif pos_75d == False and pos_15d == False and pos_165d == True and pos_105d == True:
        			position = 2
                        elif pos_75d == False and pos_15d == False and pos_165d == False and pos_105d == True:
        			position = 3
                        elif pos_75d == False and pos_15d == False and pos_165d == False and pos_105d == False:
        			position = 4
                        elif pos_75d == True and pos_15d == False and pos_165d == False and pos_105d == False:
        			position = 5
                        elif pos_75d == True and pos_15d == True and pos_165d == False and pos_105d == False:
        			position = 6
                        elif pos_75d == True and pos_15d == True and pos_165d == True and pos_105d == False:
        			position = 7
                elif state == 1:
        		if xPos <= yPos:
                                pos_45d = True
                        if (-1)*xPos <= yPos:
        			pos_135d = True
                        if xPos*xPos + yPos*yPos <= 256*256:
        			position = -1
                        elif pos_45d == True and pos_135d == True:
        			position = 0
                        elif pos_45d == False and pos_135d == True:
        			position = 1
                        elif pos_45d == False and pos_135d == False:
        			position = 2
                        elif pos_45d == True and pos_135d == False:
        			position = 3

        			
                if state == 0:
        		x_s = -1
                        y_s = -1
                        if position == -1: #no move
        			isOneclick = False;
                        else:
        			if isOneclick == False:
                                        isOneclick = True
                                        x_s = position
                                        y_s = -1
                                        state = 1
                                        window.stC = 0
                                        window.mFlagC = True
                                        window.eventCos(x_s)
                else:
        		if position == -1: #no move
                                isOneclick = False;
                        elif position == 2: #dn
        			if isOneclick == False:
                                        isOneclick = True
                                        if x_s == 6:
        					y_s = position
                                                isSelect = True
                                        else:
        					y_s = -1
                                        state = 0
                                        window.eventCos(-1)
                        else:
        			if isOneclick == False:
                                        isOneclick = True
                                        y_s = position
                                        isSelect = True
                if isOneclick == True:
                        playvoice =

		time.sleep(delay)

def keyboard2():
	print "start keyboard2"
	global window
	global R_pase
	global position_R
	global monitoroff
	global OptionState
	

	isOneclick = False
	isSelect = False
	state = 0
	pase = 0
	x_s = -1
	y_s = -1

	position = -1

	pos_75d = False
	pos_15d = False
	pos_165d = False
	pos_105d = False

	pos_45d = False
	pos_135d = False

	while True:
		xPos=ReadChannel(joy_xR) - 512
		yPos=ReadChannel(joy_yR) - 512
  
		pos_45d = False
		pos_135d = False
	
		if isSelect == True:
			isSelect = False
			if x_s < 0:
				pass
			else:
				if x_s == 0:
					device.emit_click(uinput.KEY_UP)
				elif x_s == 2:
					device.emit_click(uinput.KEY_DOWN)
				x_s = -1


		if xPos <= yPos:
			pos_45d = True
		if (-1)*xPos <= yPos:
			pos_135d = True
		if xPos*xPos + yPos*yPos <= 256*256:
			position = -1
		elif pos_45d == True and pos_135d == True:
			position = 0
		elif pos_45d == False and pos_135d == True:
			position = 1
		elif pos_45d == False and pos_135d == False:
			position = 2
		elif pos_45d == True and pos_135d == False:
			position = 3


		x_s = -1

		if position == -1: #no move
			isOneclick = False;
		else:
			if isOneclick == False:
				isOneclick = True
				x_s = position
				isSelect = True

		if OptionState == False and position == -1:
			break

	isOneclick = False
	isSelect = False
	state = 0
	pase = 0
	x_s = -1
	y_s = -1

	position = -1

	pos_75d = False
	pos_15d = False
	pos_165d = False
	pos_105d = False

	pos_45d = False
	pos_135d = False

	print "keyboardR next"

	while not window:
		time.sleep(0.1)
	
	while True:
                xPos=ReadChannel(joy_xR) - 512
                yPos=ReadChannel(joy_yR) - 512
  
                pos_75d = False  #1
                pos_15d = False  #2
                pos_165d = False  #3
                pos_105d = False  #4
                pos_45d = False
                pos_135d = False
        
                if R_pase == 0:
            
                        if isSelect == True:
        			isSelect = False
                                if x_s < 0 or y_s < 0:
        				pass
                                else:
        				if pase == 0:
                                                if ismap2[x_s][y_s] == True:
                                                        if CDataStore.Level == 2:
                                                                lock.acquire()
                                                                audioplay.audioplay("lv2.wav", 44100)
                                                                lock.release()
                                                                window.stC = 0  #cons
                                                                window.mFlagC = False
                                                                #window.eventCos(-1)
                                                                state = 0
                                                                x_s = -1
                                                                y_s = -1
                                                        elif CDataStore.Level == 3:
                                                                lock.acquire()
                                                                audioplay.audioplay("lv3.wav", 44100)
                                                                lock.release()
                                                                window.stC = 0  #cons
                                                                window.mFlagC = False
                                                                #window.eventCos(-1)
                                                                state = 0
                                                                x_s = -1
                                                                y_s = -1
                                                                #window.eventCos(-2)
                                                        else:
                                                                functionmap2[x_s][y_s](parmmap2[x_s][y_s])
                                                                if audiomap2[x_s][y_s][0] == True:
                                                                        lock.acquire()
                                                                        audioplay.audioplay(audiomap2[x_s][y_s][1])
                                                                        lock.release()
                                                                if bluemap2[x_s][y_s][0] == True:
                							#pass
                                                                        kb.send_event(bluemap2[x_s][y_s][1], 1, bt)
                                                                        kb.send_event(bluemap2[x_s][y_s][1], 0, bt)							
                                                                else:
                							#pass
                                                                        kb.send_event("KEY_LEFTSHIFT", 1, bt)
                                                                        kb.send_event(bluemap2[x_s][y_s][1], 1, bt)
                                                                        kb.send_event(bluemap2[x_s][y_s][1], 0, bt)
                                                                        kb.send_event("KEY_LEFTSHIFT", 0, bt)
                                                                #window.st = 1  #vow
                                                                window.mFlagV = False
                                                                window.eventVow(-1)
                                                                state = 0
                                                                x_s = -1
                                                                y_s = -1
                                        else:
                                                if ismap2[x_s][y_s] == True:
        						functionmap2[x_s][y_s](parmmap2[x_s][y_s])
                                                        #window.st = 1  #vow
                                                        window.mFlagV = False
                                                        window.eventVow(-1)
                                                        state = 0
                                                        x_s = -1
                                                        y_s = -1

                                                        
                        if state == 0:
        			if 3.732*xPos <= yPos: #80d = 5.671 , 75d = 3.732
                                        pos_75d = True
                                if 0.268*xPos <= yPos: #10d = 0.176 , 15d = 0.268
        				pos_15d = True
                                if -0.268*xPos <= yPos: #170d = -0.176 , 165d = -0.268
        				pos_165d = True
                                if -3.732*xPos <= yPos: #100d = -5.671 , 105d = -3.732
        				pos_105d = True        	
                                if xPos*xPos + yPos*yPos <= 256*256:
        				position = -1
                                elif pos_75d == True and pos_15d == True and pos_165d == True and pos_105d == True:
        				position = 0
                                elif pos_75d == False and pos_15d == True and pos_165d == True and pos_105d == True:
        				position = 1
                                elif pos_75d == False and pos_15d == False and pos_165d == True and pos_105d == True:
                                        position = 2
                                elif pos_75d == False and pos_15d == False and pos_165d == False and pos_105d == True:
        				position = 3
                                elif pos_75d == False and pos_15d == False and pos_165d == False and pos_105d == False:
        				position = 4
                                elif pos_75d == True and pos_15d == False and pos_165d == False and pos_105d == False:
        				position = 5
                                elif pos_75d == True and pos_15d == True and pos_165d == False and pos_105d == False:
        				position = 6
                                elif pos_75d == True and pos_15d == True and pos_165d == True and pos_105d == False:
        				position = 7
                        elif state == 1:
        			if xPos <= yPos:
                                        pos_45d = True
                                if (-1)*xPos <= yPos:
        				pos_135d = True
                                if xPos*xPos + yPos*yPos <= 256*256:
        				position = -1
                                elif pos_45d == True and pos_135d == True:
        				position = 0
                                elif pos_45d == False and pos_135d == True:
        				position = 1
                                elif pos_45d == False and pos_135d == False:
        				position = 2
                                elif pos_45d == True and pos_135d == False:
        				position = 3
        	
                        if state == 0:
        			x_s = -1
                                y_s = -1
                                if position == -1: #no move
        				isOneclick = False;
                                elif position == 4:
                                        if isOneclick == False:
                                                isOneclick = True
                                                device.emit_click(uinput.KEY_SPACE)
						kb.send_event("KEY_SPACE", 1, bt)
						kb.send_event("KEY_SPACE", 0, bt)                                                
                                else:
        				if isOneclick == False:
                                                isOneclick = True
                                                x_s = position
                                                y_s = -1
                                                state = 1
                                                if pase == 0: #cons
        						#window.st = True
                                                        window.mFlagV = True
                                                if pase == 1: #vow
        						#window.st = False
                                                        window.mFlagV = True
                                                window.eventVow(x_s)
                                position_R = position
                        else:
        			if position == -1: #no move
                                        isOneclick = False;
                                elif position == 2: #dn
        				if isOneclick == False:
                                                isOneclick = True
                                                y_s = -1
                                                state = 0
                                                window.eventVow(-1)
                                else:
        				if isOneclick == False:
                                                isOneclick = True
                                                y_s = position
                                                isSelect = True
                                position_R = position
                else: #ARROW
        		if isSelect == True:
                                isSelect = False
                                if x_s < 0:
        				pass
                                else:
        				if x_s == 0:
                                                #pass
						kb.send_event("KEY_UP", 1, bt)
						kb.send_event("KEY_UP", 0, bt)
                                        elif x_s == 1:
        					#pass
						kb.send_event("KEY_RIGHT", 1, bt)
						kb.send_event("KEY_RIGHT", 0, bt)
                                        elif x_s == 2:
        					#pass
						kb.send_event("KEY_DOWN", 1, bt)
						kb.send_event("KEY_DOWN", 0, bt)
                                        elif x_s == 3:
        					#pass
						kb.send_event("KEY_LEFT", 1, bt)
						kb.send_event("KEY_LEFT", 0, bt)
                
                        if xPos <= yPos:
        			pos_45d = True
                        if (-1)*xPos <= yPos:
        			pos_135d = True        
                        if xPos*xPos + yPos*yPos <= 256*256:
        			position = -1
                        elif pos_45d == True and pos_135d == True:
        			position = 0
                        elif pos_45d == False and pos_135d == True:
        			position = 1
                        elif pos_45d == False and pos_135d == False:
        			position = 2
                        elif pos_45d == True and pos_135d == False:
        			position = 3        
                        x_s = -1
                        if position == -1: #no move
        			isOneclick = False;
                        else:
        			if isOneclick == False:
                                        isOneclick = True
                                        x_s = position
                                        isSelect = True
                        position_R = position

		time.sleep(delay)
	
def click():
	print "start click1"
	isSWTclick = False
	global state
	global OptionState
	global Form
	
	while True:
		swt_value=ReadChannel(joy_buttonL)
		if swt_value <= 10:
                        if isSWTclick == False:
                                isSWTclick = True
                                OptionState = False
		else:
			isSWTclick = False
		if swt_value > 10 and OptionState == False:
			break
		time.sleep(delay)
		
	device.emit_click(uinput.KEY_ENTER)
	isSWTclick = False
	print "clickL next"

	while not window:
		time.sleep(0.1)

	while True:
                if True:
                        swt_value=ReadChannel(joy_buttonL)
                        if swt_value <= 10:
                                if isSWTclick == False and state == 0:
                                        isSWTclick = True
                                        device.emit_click(uinput.KEY_ENTER)
                			kb.send_event("KEY_ENTER", 1, bt)
                			kb.send_event("KEY_ENTER", 0, bt)
        		else:
                                isSWTclick = False
                time.sleep(delay)


def click2():
	print "start click2"
	isSWTclick = False
	global window
	global position_R
	global R_pase
	global OptionState


	while True:
		swt_value=ReadChannel(joy_buttonR)
		if swt_value <= 10:
                        if isSWTclick == False:
                                isSWTclick = True
		else:
			isSWTclick = False
		if swt_value > 10 and OptionState == False:
			break
		time.sleep(delay)

	isSWTclick = False
	print "clickR next"

	while not window:
		time.sleep(0.1)

	while True:
                if True:
                        swt_value=ReadChannel(joy_buttonR)
                        if swt_value <= 10:
                                if isSWTclick == False and position_R == -1:
                                        isSWTclick = True
                                        if R_pase == 0:
                				R_pase = 1
                                                window.mFlagV = True
                                                window.stV=0
                                                window.eventVow(10)
        			
                                        elif R_pase == 1:
                				R_pase = 0
                                                window.mFlagV = False
                                                window.stV = 1
                                                window.eventVow(10)
                        else:
                		isSWTclick = False
                time.sleep(delay)

def joy2keyboard():
	global cqueue
	global window
	
	while len(cqueue) < 4 or not window:
		time.sleep(delay)

	print "start joy2keyboard"
	while True:
		joy_left()
		joy_right()
		joy_lclick()
		joy_rclick()
		time.sleep(0.1)

#def getSwitchClick(swt_val):#
#	if swt_val==1:
#		device.emit_click(uinput.KEY_ENTER)


class SlideShowPics_(QtGui.QMainWindow):

	# SlideShowPics class defines the methods for UI and working logic
	def __init__(self, parent=None):
		super(SlideShowPics, self).__init__(parent)
		# self._path = path	
		self.stC = 0 #stC=0 -> consonant, st=1 -> backspace, esc key	
		self.stV = 0 #stV=0 -> vowel, stV=1 -> number
		self.monitoroff = False
		self.mFlagC = True #different main screen(consonant, each things)
		self.mFlagV = False #different main screen(vowel, each things)
		self.prepairWindow()
		self.buildUi()
		#self.changeImgC() #change consonant, backspace, esc
		#self.changeImgV() #change vowel, number
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
		self.setFixedSize(screen.width(), screen.height())
		#self.showFullScreen()
		self.buildUi()

	def buildUi(self):
		font = QtGui.QFont("UnDotum",30,QtGui.QFont.Bold,False)
		
		self.le = QLineEdit()
		self.le.setObjectName("inputText")
		self.le.setReadOnly(False)
		self.le.setFont(font)
		self.le.setTextMargins (15, 15, 15, 15)
		self.connect(self.le, SIGNAL("returnPressed()"),self.update)
		self.setMenuWidget(self.le)

		self.L00 = QtGui.QLabel() #create left label
		self.L00.setAlignment(QtCore.Qt.AlignLeft)	
		self.L01 = QtGui.QLabel() #create left label
		self.L01.setAlignment(QtCore.Qt.AlignLeft)	
		self.L02 = QtGui.QLabel() #create left label
		self.L02.setAlignment(QtCore.Qt.AlignLeft)	
		self.R01 = QtGui.QLabel() #create left label
		self.R01.setAlignment(QtCore.Qt.AlignLeft)	
		self.R02 = QtGui.QLabel() #create left label
		self.R02.setAlignment(QtCore.Qt.AlignLeft)	
		self.R03 = QtGui.QLabel() #create left label
		self.R03.setAlignment(QtCore.Qt.AlignLeft)	
		self.L10 = QtGui.QLabel() #create left label
		self.L10.setAlignment(QtCore.Qt.AlignLeft)	
		self.L11 = QtGui.QLabel() #create left label
		self.L11.setAlignment(QtCore.Qt.AlignLeft)	
		self.L12 = QtGui.QLabel() #create left label
		self.L12.setAlignment(QtCore.Qt.AlignLeft)	
		self.R10 = QtGui.QLabel() #create left label
		self.R10.setAlignment(QtCore.Qt.AlignLeft)	
		self.R11 = QtGui.QLabel() #create left label
		self.R11.setAlignment(QtCore.Qt.AlignLeft)	
		self.R12 = QtGui.QLabel() #create left label
		self.R12.setAlignment(QtCore.Qt.AlignLeft)	
		self.L20 = QtGui.QLabel() #create left label
		self.L20.setAlignment(QtCore.Qt.AlignLeft)	
		self.L21 = QtGui.QLabel() #create left label
		self.L21.setAlignment(QtCore.Qt.AlignLeft)	
		self.L22 = QtGui.QLabel() #create left label
		self.L22.setAlignment(QtCore.Qt.AlignLeft)	
		self.R20 = QtGui.QLabel() #create left label
		self.R20.setAlignment(QtCore.Qt.AlignLeft)	
		self.R21 = QtGui.QLabel() #create left label
		self.R21.setAlignment(QtCore.Qt.AlignLeft)	
		self.R22 = QtGui.QLabel() #create left label
		self.R22.setAlignment(QtCore.Qt.AlignLeft)	
		
		self.layout.addWidget(self.L00,0,0)
		self.layout.addWidget(self.L01,0,1)
		self.layout.addWidget(self.L02,0,2)
		self.layout.addWidget(self.L10,1,0)
		self.layout.addWidget(self.L11,1,1)
		self.layout.addWidget(self.L12,1,2)
		self.layout.addWidget(self.L20,2,0)
		self.layout.addWidget(self.L21,2,1)
		self.layout.addWidget(self.L22,2,2)

		self.setCentralWidget(self.centralWidget)

	def update(self):
		self.le.clear()

	def eventCos(self, event):
		self.L00.setText("%d"%event)
		self.L01.setText("%d"%event)
		self.L02.setText("%d"%event)
		self.L10.setText("%d"%event)
		self.L11.setText("%d"%event)
		self.L12.setText("%d"%event)
		self.L20.setText("%d"%event)
		self.L21.setText("%d"%event)
		self.L22.setText("%d"%event)
		pass

	def eventVow(self, event):
		pass


class SlideShowPics(QtGui.QMainWindow):

	# SlideShowPics class defines the methods for UI and working logic
	def __init__(self, parent=None):
		super(SlideShowPics, self).__init__(parent)
		# self._path = path	
		self.stC = 0 #stC=0 -> consonant, st=1 -> backspace, esc key	
		self.stV = 0 #stV=0 -> vowel, stV=1 -> number
		self.monitoroff = False
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
		self.setFixedSize(screen.width(), screen.height())
		#self.showFullScreen()
		self.buildUi()

	def buildUi(self):
		font = QtGui.QFont("UnDotum",30,QtGui.QFont.Bold,False)
		
		self.le = QLineEdit()
		self.le.setObjectName("inputText")
		self.le.setReadOnly(False)
		self.le.setFont(font)
		self.le.setTextMargins (15, 15, 15, 15)
		self.connect(self.le, SIGNAL("returnPressed()"),self.update)
		self.setMenuWidget(self.le)

		self.label = QtGui.QLabel() #create left label
		self.label.setAlignment(QtCore.Qt.AlignLeft)	
		
		self.label2 = QtGui.QLabel() #create right label
		self.label2.setAlignment(QtCore.Qt.AlignRight)
		
		self.layout.addWidget(self.label,0,0)
		self.layout.addWidget(self.label2,0,1)

		self.setCentralWidget(self.centralWidget)

	def update(self):
		self.le.clear()

	def changeImgC(self):
		# switch to main image(consonant or vowel) or second image(detail)
		self.mFlagC=True
		self.showImageByPathC('image/consonant/8basis.png')

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
		self.view_path = path
		thread = LoadImageThread()
		self.connect(thread, QtCore.SIGNAL("showImageC()"), self.showImageC)
		thread.start()

	def showImageByPathV(self, path):
		self.view_path2 = path
		thread = LoadImageThread2()
		self.connect(thread, QtCore.SIGNAL("showImageV()"), self.showImageV)
		thread.start()

	def showImageC(self):
		path = self.view_path
		image = QtGui.QImage(path)
		pp = QtGui.QPixmap.fromImage(image)
		self.label.setPixmap(pp.scaled(
				self.label.size(),
				QtCore.Qt.KeepAspectRatio,
				QtCore.Qt.SmoothTransformation))
	
	def showImageV(self):
		path2 = self.view_path2
		image2 = QtGui.QImage(path2)
		pp2 = QtGui.QPixmap.fromImage(image2)
		self.label2.setPixmap(pp2.scaled(
				self.label2.size(),
				QtCore.Qt.KeepAspectRatio,
				QtCore.Qt.SmoothTransformation))

	def eventCos(self, event):
		print self.monitoroff
		if self.monitoroff == False:
			if event == QtCore.Qt.Key_Escape:
				self.close()
	
			elif self.mFlagC==True and event == 7:
				self.mFlagC=False
				if self.stC == 0:
					self.showImageByPathC('image/consonant/8arrow.png')
	
			elif self.mFlagC==True and event == 0:
				self.mFlagC=False
				if self.stC == 0:
					self.showImageByPathC('image/consonant/1arrow.png')
	
			elif self.mFlagC==True and event == 1:
				self.mFlagC=False
				if self.stC == 0:
					self.showImageByPathC('image/consonant/2arrow.png')
	
			elif self.mFlagC==True and event == 6:
				self.mFlagC=False
				if self.stC == 0:
					self.showImageByPathC('image/consonant/esc.png')
	
			elif self.mFlagC==True and event == 2:
				self.mFlagC=False
				if self.stC == 0:
					self.showImageByPathC('image/consonant/3arrow.png')
	
			elif self.mFlagC==True and event == 5:
				self.mFlagC=False
				if self.stC == 0:
					self.showImageByPathC('image/consonant/6arrow.png')
	
			elif self.mFlagC==True and event == 4:
				self.mFlagC=False
				if self.stC == 0:
					self.showImageByPathC('image/consonant/5arrow.png')

			elif self.mFlagC==True and event == 3:
				self.mFlagC=False
				if self.stC == 0:
					self.showImageByPathC('image/consonant/4arrow.png')
	
			elif self.mFlagC==False:
				if event == -2:
					self.showImageByPathC('image/consonant/black.jpg')
					self.showImageByPathV('image/vowel/black.jpg')
				else:
					self.changeImgC()
			
	def eventVow(self, event):
		if self.monitoroff == False:
			if self.mFlagV==True and event == 7:
				self.mFlagV=False
				if self.stV == 0:
					self.showImageByPathV('image/vowel/8arrow.png')
	
			elif self.mFlagV==True and event == 0:
				self.mFlagV=False
				if self.stV == 0:
					self.showImageByPathV('image/vowel/1arrow.png')
	
			elif self.mFlagV==True and event == 1:
				self.mFlagV=False
				if self.stV == 0:
					self.showImageByPathV('image/vowel/2arrow.png')
	
			elif self.mFlagV==True and event == 6:
				self.mFlagV=False
				if self.stV == 0:
					self.showImageByPathV('image/vowel/7arrow.png')
	
			elif self.mFlagV==True and event == 2:
				self.mFlagV=False
				if self.stV == 0:
					self.showImageByPathV('image/vowel/3arrow.png')
	
			elif self.mFlagV==True and event == 5:
				self.mFlagV=False
				if self.stV == 0:
					self.showImageByPathV('image/vowel/6arrow.png')
	
			elif self.mFlagV==True and event == 3:
				self.mFlagV=False
				if self.stV == 0:
					self.showImageByPathV('image/vowel/4arrow.png')
	
			elif self.mFlagV==True and event == 10:#click
				self.mFlagV=False
				if self.stV == 0:
					self.stV = 1
					self.changeImgV()
	
			elif self.mFlagV==False:
				if self.stV == 0:		
					if event == -1 or event == 4 or event == 6 or event == 0 or event == 2:	#change main screen after insert
						self.changeImgV()
				elif self.stV == 1:
					if event == 10: #click
						self.stV = 0
						self.changeImgV()



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

	def keyPressEvent(self, e):
		if e.key() == QtCore.Qt.Key_Return:
			self.setting_button_click()
			QtCore.QCoreApplication.instance().quit()
		else:
			e.accept()


class LoadImageThread(QtCore.QThread):
	trigger = QtCore.pyqtSignal(int)
	def __init__(self):
		QtCore.QThread.__init__(self)
	def __del__(self):
		self.wait()

	def run(self):
		self.emit(QtCore.SIGNAL('showImageC()'))

class LoadImageThread2(QtCore.QThread):
	trigger = QtCore.pyqtSignal(int)
	def __init__(self):
		QtCore.QThread.__init__(self)
	def __del__(self):
		self.wait()

	def run(self):
		self.emit(QtCore.SIGNAL('showImageV()'))


def main():
	global window
	global Form
	global bt
	global kb
	global app

	bt = PiTooth.Bluetooth()
	bt.listen()
	kb = PiTooth.Keyboard()
	testfile = "test1.json"
        mode = 0
        if len(sys.argv) <= 1:
                print "plese select Mode"
                exit()
        elif sys.argv[1] == "test": #0
                mode = 0
                if len(sys.argv) <= 2:
                        print "input test file"
                        exit()
                else:
                        testfile = sys.argv[2]
        elif sys.argv[1] == "ex": #1
                mode = 1
        else:
                print "invalid option"
                exit()

	#Form.setAlignment(QtCore.Qt.AlignCenter)
	# Create and display the splash screen
	app = QtGui.QApplication(sys.argv)
	app2 = QtGui.QApplication(sys.argv)
	#app2 = QtGui.QApplication(sys.argv)


	start = time.time()
	splash_pix = QPixmap('image/splash.jpg')
	splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
	splash.setMask(splash_pix.mask())
	splash.show()
	while time.time() - start < 1:
		time.sleep(0.001)
		app.processEvents()

	time.sleep(3)


    # Simulate something that takes time


	#Form = QtGui.QWidget()
	Form = QtGui.QMainWindow()
	Form.resize(400, 300)

	ui = Ui_Form()
	Form.setCentralWidget(ui)
	Form.show()
	splash.finish(Form)


	th0=threading.Thread(target=SpiChannelLoop)
	th0.start()
	th=threading.Thread(target=keyboard)
	th.start()
	th2=threading.Thread(target=click)
	th2.start()
	th3=threading.Thread(target=keyboard2)
	th3.start()
	th4=threading.Thread(target=click2)
	th4.start()

	#th5=threading.Thread(target=joy2keyboard)
	#th5.start()

	app2.exec_()

	start = time.time()
	splash_pix = QPixmap('image/splash2.jpg')
	splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
	splash.setMask(splash_pix.mask())
	splash.show()
	while time.time() - start < 1:
		time.sleep(0.001)
		app.processEvents()

	obd = threading.Thread(target=obdMain.obdMainCode, args = (mode,testfile))
	obd.start()

	window = SlideShowPics()
	window.show()
	splash.finish(window)
	window.raise_()
	app.exec_()

	#Form = QtGui.QWidget()
	#ui = optionUI.Ui_Form()
	#ui.setupUi(Form)
	#Form.show()
	#splash.finish(Form)
#	window = SlideShowPics()
#	splash.finish(window)
#	window.show()
#	window.raise_()

#	window = SlideShowPics()
#	app2.exec_()




#	app.exec_()

if __name__ == '__main__':
	main()












