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
        #///////////////// ���⿡ �о�� �����͸� OBD2 ��ü�� �� �ִ� �۾��� �ۼ��Ѵ�.
            #���⿡ pyOBD��ü�κ��� �����͸� �о���� �ڵ带 �ۼ�
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
    analysis.ModuleList = moduleList #����ϴ� ������ ������ �ٸ� ��⿡�� ���� �˷��־�� �Ѵ�.
    obd2test = pyOBDReader()
    try:
        #���� �ʱ�ȭ�� ��� import������ ���������� ���� �ʿ��� �����带 ���� ��Ų��.
        #gpsp.start() # start it up
        obd2test.start()
        
        while True: #3�ʿ� �ѹ��� ���� ���¿� ���� �м��� �õ��Ѵ�.
            #It may take a second or two to get good data
            analysis.AnalysisReq()            
            #gpsd.fix.latitude, gpsd.fix.longitude
            time.sleep(2) #while���� ���鼭 2�ʿ� �ѹ��� ���� ���¿� ���� �м��� �õ��Ѵ�.
 
    except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
        print "\nKilling Thread..."
        gpsp.running = False
        gpsp.join() # wait for the thread to finish what it's doing
    print "Done.\nExiting."
