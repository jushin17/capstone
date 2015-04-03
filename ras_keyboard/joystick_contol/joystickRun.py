#!/usr/bin/python
#--------------------------------------
#
# Author : Matt Hawkins
# Date   : 17/04/2014
#
#--------------------------------------
 
import spidev
import time
import os
 
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)		# it will open /dev/spidev-0.0
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
 
# Define sensor channels
# (channels 3 to 7 unused)
swt_channel = 0
vrx_channel = 1
vry_channel = 2
 
# Define delay between readings (s)
delay = 0.01
 
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

while True:
 
  # Read the joystick position data
  vrx_pos = ReadChannel(vrx_channel)
  vry_pos = ReadChannel(vry_channel)
 
  # Read switch state
  swt_val = ReadChannel(swt_channel)

  dir=getDirection(vrx_pos, vry_pos)
  swt=getSwitchClick(swt_val)

  # Wait before repeating loop
  time.sleep(delay) 