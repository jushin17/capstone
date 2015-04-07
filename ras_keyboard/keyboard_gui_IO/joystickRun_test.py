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
 
import spidev
import time
import os
 
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

def getDirection(xPos, yPos):
  if 341<xPos and xPos<682 and 341<yPos and yPos<682:
    dir="no move"
  elif 341<=xPos and xPos<=682 and yPos>=682:
    dir="UP"
  elif 341<=xPos and xPos<=682 and yPos<=341:
    dir="DN"
  elif xPos<=341 and 341<=yPos and yPos<=682:
    dir="LF"
  elif xPos>=682 and 341<=yPos and yPos<=682:
    dir="RT"
  elif xPos<341 and yPos>682:
    dir="UL"
  elif xPos<341 and yPos<341:
    dir="DL"
  elif xPos>682 and yPos>682:
    dir="UR"
  elif xPos>682 and yPos<341:
    dir="DR"
  return dir

def getSwitchClick(swt_val):
  if swt_val==1:
    return 1
  return 0

def test(swt_channel, vrx_channel, vry_channel): 
	while True:
	 
	  # Read the joystick position data
	  vrx_pos = ReadChannel(vrx_channel)
	  vry_pos = ReadChannel(vry_channel)
	 
	  # Read switch state
	  swt_val = ReadChannel(swt_channel)
	  
	  dir=getDirection(vrx_pos, vry_pos)
  	  swt=getSwitchClick(swt_val)

	  if (not fire) and (not swt!=1):  # player 1 Fire button pressed
	    fire = True
	    device.emit(uinput.KEY_SPACE, 1) # player 1 Press space bar

	  if fire and swt==0:  # player 1 Fire button released
	    fire = False
	    device.emit(uinput.KEY_SPACE, 0) # player 1 Release space bar

	  if (not up) and (not dir!="UP"):  # player 1 Up button pressed
	    up = True
	    device.emit(uinput.KEY_UP, 1) # player 1 Press Up key

	  if up and dir=="UP":  # player 1 Up button released
	    up = False
	    device.emit(uinput.KEY_UP, 0) # player 1 Release Up key

	  if (not down) and (not dir=="DN"):  # player 1 Down button pressed
	    down = True
	    device.emit(uinput.KEY_DOWN, 1) # player 1 Press Down key

	  if down and dir!="DN":  # player 1 Down button released
	    down = False
	    device.emit(uinput.KEY_DOWN, 0) # player 1 Release Down key

	  if (not left) and (not dir=="LF"):  # player 1 Left button pressed
	    left = True
	    device.emit(uinput.KEY_LEFT, 1) # player 1 Press Left key

	  if left and dir!="LF":  # player 1 Left button released
	    left = False
	    device.emit(uinput.KEY_LEFT, 0) # player 1 Release Left key

	  if (not right) and (not dir=="RT"):  # player 1 Right button pressed
	    right = True
	    device.emit(uinput.KEY_RIGHT, 1) # player 1 Press Right key

	  if right and dir!="RT":  # player 1 Right button released
	    right = False
	    device.emit(uinput.KEY_RIGHT, 0) # player 1 Release Right key
   	  
	  
	  # Wait before repeating loop
	  time.sleep(delay)

# Define sensor channels
# (channels 3 to 7 unused)
swt_channel = 0
vrx_channel = 1
vry_channel = 2
 
# Define delay between readings (s)
delay = 0.5

test(swt_channel, vrx_channel, vry_channel)
