# -*- coding: cp949 -*-

import DataStore
from DataStore import CDataStore
from programOption import CSetting


class DataScore:
    #score = {'speed': 0, 'steering': 0, 'rain': 0, 'snow':0 ,'gear':0}
    def __init__(self):  #datalist �� Dict���̴�
        pass
            
#    def setScore(self, dataname, data):
#        if dataname in DataScore.datalist:
#            DataScore.datalist[dataname] = data
            
    def calcScore(self):
        pass
    

class SpeedScore(DataScore): #speed
    def __init__(self):
        DataScore.__init__(self)
        DataStore.CDataStore.ScoreData['speed'] = -1
    def calcScore(self):
        result = -1
        result = DataStore.CDataStore.SensorData['speed']
        
        if CSetting.SpeedStand[1] <= result <= CSetting.SpeedStand[2]:
            DataStore.CDataStore.ScoreData['speed'] = 80
        elif CSetting.SpeedStand[2] < result:
            DataStore.CDataStore.ScoreData['speed'] = 100
        else:
            DataStore.CDataStore.ScoreData['speed'] = result


class GearScore(DataScore): #gear
    def __init__(self):    #driveMode ó���� ���� ����ϰ� �����غ���
        DataScore.__init__(self)
        DataStore.CDataStore.ScoreData['gear'] = -1
    def calcScore(self):
        gear = DataStore.CDataStore.SensorData['gear']
        driveMode = {'parking' : 1, 'drive': 2, 'back': 3}
        result = -1
        #if gear == driveMode['parking']:
        if gear == driveMode['parking']:
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
        DataStore.CDataStore.ScoreData['rain'] = -1
    def calcScore(self):
        rain = DataStore.CDataStore.SensorData['rain']
        result = -1
        if 0 < rain <= 1:
            result = 0
        elif 1 < rain <= 5:
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
        DataStore.CDataStore.ScoreData['snow'] = -1
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
        DataStore.CDataStore.ScoreData['steering']  = -1
    def calcScore(self):
        turnsig = DataStore.CDataStore.SensorData['steering']
        result = 0
        if turnsig > 10.0:
            result = 100
        else:
            result = 0
        DataStore.CDataStore.ScoreData['steering'] = result

def initAnalysis():   #�ϳ��� Score��� ������ �߰��ɶ����� class�� �߰��ϰ� �̰����� �ʱ�ȭ �Ѵ�
    global DataScoreList
    DataScoreList.append(SpeedScore())
    DataScoreList.append(GearScore())
    DataScoreList.append(RainScore())
    DataScoreList.append(SnowScore())
    DataScoreList.append(SteeringScore())
    
    
def AnalysisReq():
    for ds in DataScoreList:  #���� ������ ����ҿ� �̹� ������Ʈ �� �����͵��� �ֱ⶧���� �ٷ� ���ھ ����ϸ� �ȴ�.
        if DataStore.CDataStore.isChanged() == True:
            ds.calcScore()
    #print DataScore.datalist, 'datalist'
    #print DataScore.score, 'score'
    return
DataScoreList = []
initAnalysis()
    

        

        
                
    
    
