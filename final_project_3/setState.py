# -*- coding: cp949 -*-
from DataStore import CDataStore

class CGetData(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.current_value = None
        self.running = True
        return

    def run(self):
        while True:
            print "Select Set State"
            print "0 : Speed"
            print "1 : Steering"
            print "2 : Gear"
            print "3 : Rain"
            print "4 : Road"
            state = -1
            setVal = False
            if state == 0:
                CDataStore.StateSpeed = setVal
            if state == 1:
                CDataStore.StateSteering = setVal
            if state == 2:
                CDataStore.StateGear = setVal
            if state == 3:
                CDataStore.StateRain = setVal
            if state == 4:
                CDataStore.StateRoad = setVal
            else:
                print "input error"
            
                
                
            
