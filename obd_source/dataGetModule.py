# -*- coding: cp949 -*-
import time

class DataDev:
    def __init__(self):
        return

    def getDataList(self):
        return self.datalist
    def isChanged(self): #일단 무조건 True로 returns
        return True

    def updateData(self):
        return
    
class OBD2(DataDev):
    def __init__(self):
        DataDev.__init__(self)
        self.datalist = {'speed': 0, 'turnsignal': 0, 'gear':0}
        
    def updateData(self, speed, turnsignal, gear):
        self.datalist['speed'] = speed
        self.datalist['turnsignal'] = turnsignal
        self.datalist['gear'] = gear
        return
        
class Weather(DataDev):
    def __init__(self):
        DataDev.__init__(self)
        self.datalist = {'rain': 0, 'snow':0}

    def updateData(self):
        return 
        
class Road(DataDev):
    def __init__(self):
        DataDev.__init__(self)
        self.datalist = {'roadtype': 0}

  
    def updateData(self):
        return

      



def getModuleList():
    global moduleList
    return moduleList


