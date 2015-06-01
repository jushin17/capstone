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
import DataStore
#import setState.py

os.system('clear') #clear the terminal (optional)

def obdMainCode(mode, filename):  # 0 == test, 1 == ex

    #testmode
    if mode == 0:
        testmode = programOption.TESTMODE
    elif mode == 1:
        testmode = programOption.EXMODE
    #obdmode
    #gpsmode
    #roadmode
    #wethermode
    #keyboardmode
    #etc....

    #######################

    print 'set mode'
    programOption.StartSetMode(testmode)  #설정 파일의 내용을 프로그램 옵션으로 설정


    
    #장치객체를 생성하는 부분. 장치 객체가 생성되면 장치로부터 데이터를 읽을 준비가 완료 된 것이다. 바로 데이터를 읽으면 된다.
    print 'get pyDOBReader'
    obd2p = dataGetModule.pyOBDReader(filename) #pyOBD로 데이터 읽는 객체 생성 -> 객체 생성이 완료되면 리턴 되어야 한다.  #하나 완료될때마다 로딩 화면이 바뀌면 좋음
    print 'get GpsPoller'
    gpsp = dataGetModule.GpsPoller()  #GPS 데이터 읽는 객체 생성
    print 'get CGetWeatherData'
    weatherp = dataGetModule.CGetWeatherData()  #GPS 데이터를 이용하여 날씨를 받아오는 객체 생성print 'set mode'
    print 'CGetRoadData'
    roadp = dataGetModule.CGetRoadData()  #GmPS 데이터를 이용하여 도로 정보를 받아오는 객체 생성
    print 'finish Load dataGetModule'
    
    try:
        #먼저 초기화의 경우 import문에서 수행했으며 이제 필요한 쓰레드를 실행 시킨다.
        gpsp.start() # start it up
        obd2p.start()
        weatherp.start()
        roadp.start()

        #여기까지 진행하면 상태 분석을 위한 준비가 끝난 상태이다
        
        isLoad_Finish = True;
        print 'start program'

        sleep(3) #3초정도 여유를 둔다

        while True: #3초에 한번씩 현재 상태에 대한 분석을 시도한다.
            #It may take a second or two to get good data
            analysis.AnalysisReq()
            judge.SumScore.calculData()
            judge.SumScore.jugement()
            print 'Level : ', DataStore.CDataStore.Level
                        
            #gpsd.fix.latitude, gpsd.fix.longitude
            time.sleep(2) #while문을 돌면서 1초에 한번씩 현재 상태에 대해 분석을 시도한다.
            
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
