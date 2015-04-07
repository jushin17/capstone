#!/usr/bin/python
#--------------------------------------
# This script reads data from a
# MCP3008 ADC device using the SPI bus.
#
# Analogue joystick version!
#
# Author : Matt Hawkins
# Date   : 17/04/2014
# User : Seo Junkyo/Kookmin Univ.
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

import uinput
import spidev
import time
import os

device =uinput.Device([uinput.KEY_LEFT,
		       uinput.KEY_RIGHT,
		       uinput.KEY_UP,
		       uinput.KEY_DOWN,
		       uinput.KEY_SPACE
                       ])

joy_x=1
joy_y=2
joy_button=0

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

	
# Define sensor channels
# (channels 3 to 7 unused)

 
# Define delay between readings (s)
delay = 0.25

def keyboard(): 
	while True:
	    joy_x_value=ReadChannel(joy_x)
	    joy_y_value=ReadChannel(joy_y)

	    if joy_x_value<500: 
	      device.emit(uinput.KEY_LEFT,1)
	      device.emit(uinput.KEY_LEFT,0)
	    elif joy_x_value>540: 
	      device.emit(uinput.KEY_RIGHT,1)
	      device.emit(uinput.KEY_RIGHT,0)

	    if joy_y_value<500: 
	      device.emit(uinput.KEY_DOWN,1)
	      device.emit(uinput.KEY_DOWN,0)
	    elif joy_y_value>540: 
	      device.emit(uinput.KEY_UP,1)
	      device.emit(uinput.KEY_UP,0)

    	    time.sleep(delay)

def click(): 
	while True:
	    swt_value=ReadChannel(joy_button)
		    
	    if swt_value==1: 
	      device.emit(uinput.KEY_SPACE,1)
	      device.emit(uinput.KEY_SPACE,0)

	    time.sleep(0.12)
