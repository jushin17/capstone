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
import read
import json
import judge

 
gpsd = None #seting the global variable

os.system('clear') #clear the terminal (optional)
 
class GpsPoller(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        ##global gpsd #bring it in scope
        ##gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
        self.current_value = None
        self.running = True #setting the thread running to true
 
    def run(self):
        global moduleList
        global gpsd
        #while gpsp.running:
        if mode == TESTMODE:
            gpsfile = file('testgps.txt')
            line = gpsfile.readline()
            while line:
                #���⿡ gpsd���� ��� �����͸� �о���� �ڵ带 �ۼ�
                lst = line.split() #lat, lon
                dataGetList['weather'].updatelatlon(lst[0], lst[1])
                dataGetList['Road'].updatelatlon(lst[0], lst[1])
                sleep(4)
                line = gpsfile.readline()
                print lst[0], lst[1]
                
        ##    gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer
        


class pyOBDReader(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.current_value = None
        self.running = True #setting the thread running to true
 
    def run(self):
        global moduleList
        global mode
        txtfile = file('testobd.txt')
        line = txtfile.readline()
        if mode == TESTMODE:
            with open('test.json') as f:
            for line in f:
                test = json.loads(line)
                if(test['name']=='vehicle_speed'):
                    dataGetList['obd2'].updateData(speed = test['value'])
                elif(test['name']=='transmission_gear_position'):
                    dataGetList['obd2'].updateData(gear = test['value'])
                elif(test['name']=='steering_wheel_angle'):
                    dataGetList['obd2'].updateData(steering = test['value'])
                sleep(1)       

dataGetList = {'obd2': dataGetModule.OBD2(), 'weather': dataGetModule.Weather(), 'road':dataGetModule.Road()}


mode = 0
TESTMODE = 0
EXMODE = 1

if __name__ == '__main__':
    mode = TESTMODE
    #gpsp = GpsPoller() # create the thread
    analysis.DataGetList = dataGetList #����ϴ� ������ ������ �ٸ� ��⿡�� ���� �˷��־�� �Ѵ�.
    obd2test = pyOBDReader()
    gpstest = GpsPoller()  #�׽�Ʈ �ڵ�
    try:
        #���� �ʱ�ȭ�� ��� import������ ���������� ���� �ʿ��� �����带 ���� ��Ų��.
        #gpsp.start() # start it up
        obd2test.start()
        gpstest.start()
        #Weathertest.start()
        
        while True: #3�ʿ� �ѹ��� ���� ���¿� ���� �м��� �õ��Ѵ�.
            #It may take a second or two to get good data
            analysis.AnalysisReq()
            judge.SumScore.calculData()
            judge.SumScore.jugement()
            print judge.SumScore.level           
                        
            #gpsd.fix.latitude, gpsd.fix.longitude
            time.sleep(2) #while���� ���鼭 2�ʿ� �ѹ��� ���� ���¿� ���� �м��� �õ��Ѵ�.
            
    except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
        print "\nKilling Thread..."
        gpsp.running = False
        gpsp.join() # wait for the thread to finish what it's doing
    print "Done.\nExiting."
