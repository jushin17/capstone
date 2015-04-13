# -*- coding: cp949 -*-

import DataStore
from DataStore import CDataStore


class DataScore:
    #score = {'speed': 0, 'steering': 0, 'rain': 0, 'snow':0 ,'gear':0}
    def __init__(self):  #datalist 는 Dict형이다
        pass
            
#    def setScore(self, dataname, data):
#        if dataname in DataScore.datalist:
#            DataScore.datalist[dataname] = data
            
    def calcScore(self):
        pass
    


class SpeedScore(DataScore): #speed
    def __init__(self):
        DataScore.__init__(self)
    def calcScore(self):
        result = -1
        result = DataStore.CDataStore.SensorData['speed']
        DataStore.CDataStore.ScoreData['speed'] = result
    

class GearScore(DataScore): #gear
    def __init__(self):    #driveMode 처리를 좀더 깔끔하게 생각해보기
        DataScore.__init__(self)
    def calcScore(self):
        gear = DataStore.CDataStore.SensorData['gear']
        driveMode = {'parking' : 1, 'drive': 2, 'back': 3}
        result = -1
        #if gear == driveMode['parking']:
        if gear == driveMode['back']:
            result = 0
        elif gear == driveMode['drive']:
            result = 20
        elif gear == driveMode['back']:
            result = 100
        else:
            result = -1
        DataStore.CDataStore.ScoreData['gear'] = result

        
class RainScore(DataScore): #rain
    def __init__(self):
        DataScore.__init__(self)
    def calcScore(self):
        rain = DataStore.CDataStore.SensorData['rain']
        result = -1
        if 0 <= rain <= 5:
            result = 10
        elif 5 <= rain <= 20:
            result = 40
        elif 20 <= rain <= 80:
            result = 60
        elif rain > 80:
            result = 100
        else:
            result = -1
        DataStore.CDataStore.ScoreData['rain'] = result

class SnowScore(DataScore): #snow
    def __init__(self):
        DataScore.__init__(self)
    def calcScore(self):
        snow = DataStore.CDataStore.SensorData['snow']
        result = -1
        if 0 <= snow <= 1:
            result = 10
        elif 1 <= snow <= 5:
            result = 40
        elif 5 <= snow <= 20:
            result = 60
        elif snow > 20:
            result = 100
        else:
            result = -1
        DataStore.CDataStore.ScoreData['snow'] = result

class SteeringScore(DataScore): #turnsignal
    def __init__(self):
        DataScore.__init__(self)
    def calcScore(self):
        turnsig = DataStore.CDataStore.SensorData['steering']
        result = 0
        if turnsig != 0:
            result = 100
        else:
            result = 0
        DataStore.CDataStore.ScoreData['steering'] = result

def initAnalysis():   #하나의 Score계산 과정이 추가될때마다 class를 추가하고 이곳에서 초기화 한다
    global DataScoreList
    DataScoreList.append(SpeedScore())
    DataScoreList.append(GearScore())
    DataScoreList.append(RainScore())
    DataScoreList.append(SnowScore())
    DataScoreList.append(SteeringScore())
    
    
def AnalysisReq():
    for ds in DataScoreList:  #이제 데이터 저장소에 이미 업데이트 된 데이터들이 있기때문에 바로 스코어를 계산하면 된다.
        if DataStore.CDataStore.isChanged() == True:
            ds.calcScore()
    #print DataScore.datalist, 'datalist'
    #print DataScore.score, 'score'
    return
DataScoreList = []
initAnalysis()
    

        

        
                
    
    
