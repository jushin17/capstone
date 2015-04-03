#!/usr/bin/python
#--------------------------------------
#
# Author : Yang Honam
# Date   : 03/04/2015
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
 
def getDirection():

  while True:
 
    # Read the joystick position data
    vrx_pos = ReadChannel(vrx_channel)
    vry_pos = ReadChannel(vry_channel)
 
    # Get direction of joystick
    if 341<vrx_pos and vrx_pos<682 and 341<vry_pos and vry_pos<682:
      dir="no move"
    elif 341<=vrx_pos and vrx_pos<=682 and vry_pos>=682:
      dir="UP"
    elif 341<=vrx_pos and vrx_pos<=682 and vry_pos<=341:
      dir="DN"
    elif vrx_pos<=341 and 341<=vry_pos and vry_pos<=682:
      dir="LF"
    elif vrx_pos>=682 and 341<=vry_pos and vry_pos<=682:
      dir="RT"
    elif vrx_pos<341 and vry_pos>682:
      dir="UL"
    elif vrx_pos<341 and vry_pos<341:
      dir="DL"
    elif vrx_pos>682 and vry_pos>682:
      dir="UR"
    elif vrx_pos>682 and vry_pos<341:
      dir="DR"

    if dir!="no move"
      return dir
    
    # Wait before repeating loop
    time.sleep(delay) 


def getSwitchState():
  while True:
 
    # Read switch state
    swt_val = ReadChannel(swt_channel)

    # Get switch state
    if swt_val==0:
      return 1

    # Wait before repeating loop
    time.sleep(delay)
