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
    programOption.StartSetMode(testmode)  #���� ������ ������ ���α׷� �ɼ����� ����


    
    #��ġ��ü�� �����ϴ� �κ�. ��ġ ��ü�� �����Ǹ� ��ġ�κ��� �����͸� ���� �غ� �Ϸ� �� ���̴�. �ٷ� �����͸� ������ �ȴ�.
    print 'get pyDOBReader'
    obd2p = dataGetModule.pyOBDReader(filename) #pyOBD�� ������ �д� ��ü ���� -> ��ü ������ �Ϸ�Ǹ� ���� �Ǿ�� �Ѵ�.  #�ϳ� �Ϸ�ɶ����� �ε� ȭ���� �ٲ�� ����
    print 'get GpsPoller'
    gpsp = dataGetModule.GpsPoller()  #GPS ������ �д� ��ü ����
    print 'get CGetWeatherData'
    weatherp = dataGetModule.CGetWeatherData()  #GPS �����͸� �̿��Ͽ� ������ �޾ƿ��� ��ü ����print 'set mode'
    print 'CGetRoadData'
    roadp = dataGetModule.CGetRoadData()  #GmPS �����͸� �̿��Ͽ� ���� ������ �޾ƿ��� ��ü ����
    print 'finish Load dataGetModule'
    
    try:
        #���� �ʱ�ȭ�� ��� import������ ���������� ���� �ʿ��� �����带 ���� ��Ų��.
        gpsp.start() # start it up
        obd2p.start()
        weatherp.start()
        roadp.start()

        #������� �����ϸ� ���� �м��� ���� �غ� ���� �����̴�
        
        isLoad_Finish = True;
        print 'start program'

        sleep(3) #3������ ������ �д�

        while True: #3�ʿ� �ѹ��� ���� ���¿� ���� �м��� �õ��Ѵ�.
            #It may take a second or two to get good data
            analysis.AnalysisReq()
            judge.SumScore.calculData()
            judge.SumScore.jugement()
            print 'Level : ', DataStore.CDataStore.Level
                        
            #gpsd.fix.latitude, gpsd.fix.longitude
            time.sleep(2) #while���� ���鼭 1�ʿ� �ѹ��� ���� ���¿� ���� �м��� �õ��Ѵ�.
            
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