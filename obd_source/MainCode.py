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
 
gpsd = None #seting the global variable

os.system('clear') #clear the terminal (optional)
 
class GpsPoller(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        global gpsd #bring it in scope
        gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
        self.current_value = None
        self.running = True #setting the thread running to true
 
    def run(self):
        global gpsd
        while gpsp.running:
            gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer


class pyOBDReader(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.current_value = None
        self.running = True #setting the thread running to true
 
    def run(self):
        global moduleList
        txtfile = file('testobd.txt')
        line = txtfile.readline()
        while line:
        #///////////////// 여기에 읽어온 데이터를 OBD2 객체에 써 넣는 작업을 작성한다.
            #여기에 pyOBD객체로부터 데이터를 읽어오는 코드를 작성
            #///////////////// ///////////////// 
            lst = line.split()
            moduleList['obd2'].updateData(int(lst[0]), int(lst[1]), int(lst[2]))
        #/////////////
            sleep(4)
            line = txtfile.readline()
        

#moduleList = {'obd2': OBD2(), 'weather': Weather(), 'road': Road()]
moduleList = {'obd2': dataGetModule.OBD2()}

if __name__ == '__main__':
    #gpsp = GpsPoller() # create the thread
    analysis.ModuleList = moduleList #사용하는 모듈들의 종류를 다른 모듈에도 전부 알려주어야 한다.
    obd2test = pyOBDReader()
    try:
        #먼저 초기화의 경우 import문에서 수했했으며 이제 필요한 쓰레드를 실행 시킨다.
        #gpsp.start() # start it up
        obd2test.start()
        
        while True: #3초에 한번씩 현재 상태에 대한 분석을 시도한다.
            #It may take a second or two to get good data
            analysis.AnalysisReq()            
            #gpsd.fix.latitude, gpsd.fix.longitude
            time.sleep(2) #while문을 돌면서 2초에 한번씩 현재 상태에 대해 분석을 시도한다.
 
    except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
        print "\nKilling Thread..."
        gpsp.running = False
        gpsp.join() # wait for the thread to finish what it's doing
    print "Done.\nExiting."
