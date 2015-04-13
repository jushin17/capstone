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
    gpsp = dataGetModule.GpsPoller()  #테스트 코드

    sleep(3)
    
    weatherp = dataGetModule.CGetWeatherData()
    roadp = dataGetModule.CGetRoadData()
    #gpsp = GpsPoller() # create the thread
    
    
    try:
        #먼저 초기화의 경우 import문에서 수했했으며 이제 필요한 쓰레드를 실행 시킨다.
        gpsp.start() # start it up
        obd2p.start()
        weatherp.start()
        roadp.start()

        while True: #3초에 한번씩 현재 상태에 대한 분석을 시도한다.
            #It may take a second or two to get good data
            analysis.AnalysisReq()
            judge.SumScore.calculData()
            judge.SumScore.jugement()
            print DataStore.CDataStore.Level
                        
            #gpsd.fix.latitude, gpsd.fix.longitude
            time.sleep(2) #while문을 돌면서 2초에 한번씩 현재 상태에 대해 분석을 시도한다.
            
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
