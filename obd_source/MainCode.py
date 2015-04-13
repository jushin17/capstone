# -*- coding: cp949 -*-
#! /usr/bin/python
# Written by Dan Mandle http://dan.mandle.me September 2012
# License: GPL 2.0
 
import os
#from gps import *
from time import *
import time
import threading
import dataGetModule
import analysis
import json
import judge
import programOption

os.system('clear') #clear the terminal (optional)

if __name__ == '__main__':

    programOption.setMode(programOption.TESTMODE)
  
    obd2p = dataGetModule.pyOBDReader()
    gpsp = dataGetModule.GpsPoller()  #�׽�Ʈ �ڵ�

    sleep(3)
    
    weatherp = dataGetModule.CGetWeatherData()
    roadp = dataGetModule.CGetRoadData()
    #gpsp = GpsPoller() # create the thread
    
    
    try:
        #���� �ʱ�ȭ�� ��� import������ ���������� ���� �ʿ��� �����带 ���� ��Ų��.
        gpsp.start() # start it up
        obd2p.start()
        weatherp.start()
        roadp.start()

        while True: #3�ʿ� �ѹ��� ���� ���¿� ���� �м��� �õ��Ѵ�.
            #It may take a second or two to get good data
            analysis.AnalysisReq()
            judge.SumScore.calculData()
            judge.SumScore.jugement()
            print DataStore.CDataStore.Level
                        
            #gpsd.fix.latitude, gpsd.fix.longitude
            time.sleep(2) #while���� ���鼭 2�ʿ� �ѹ��� ���� ���¿� ���� �м��� �õ��Ѵ�.
            
    except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
        print "\nKilling Thread..."
        gpsp.running = False
        obd2p.running = False
        weatherp.running = False
        roadp.running = False
        gpsp.join() # wait for the thread to finish what it's doing
        obd2p.join()
        weatherp.join()
        roadp.join()
    print "Done.\nExiting."
