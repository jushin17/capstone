# -*- coding: cp949 -*-

import dataGetModule

class DataScore:
    datalist = {} #class member�� ����
    score = {'speed': 0, 'turnsignal': 0, 'rain': 0, 'snow':0 ,'gear':0}
    def __init__(self, dataname):  #datalist �� Dict���̴�
        DataScore.datalist[dataname] = -1
        
    def initScore(self):
        for dl in DataScore.datalist:
            DataScore.datalist[dl] = -1
            
    def getScore(self, dataname):
            if dataname in DataScore.datalist:
                return DataScore.datalist[dataname]
            else:
                return -1
            
    def setScore(self, dataname, data):
        if dataname in DataScore.datalist:
            DataScore.datalist[dataname] = data
            
    def calcScore(self):
        pass
    


class SpeedScore(DataScore): #speed
    def __init__(self, dataname):
        DataScore.__init__(self, dataname)
    def calcScore(self):
        result = -1
        result = DataScore.datalist['speed']
        DataScore.score['speed'] = result
    

class GearScore(DataScore): #gear
    def __init__(self, dataname):    #driveMode ó���� ���� ����ϰ� �����غ���
        DataScore.__init__(self, dataname)
    def calcScore(self):
        gear = DataScore.datalist['gear']
        driveMode = {'parking' : 1, 'drive': 2, 'back': 3}
        result = -1
        if gear == driveMode['parking']:
            result = 0
        elif gear == driveMode['drive']:
            result = 20
        elif gear == driveMode['back']:
            result = 100
        else:
            result = -1
        DataScore.score['gear'] = result

        
class RainScore(DataScore): #rain
    def __init__(self, dataname):
        DataScore.__init__(self, dataname)
    def calcScore(self):
        rain = DataScore.datalist['rain']
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
        DataScore.score['rain'] = result

class SnowScore(DataScore): #snow
    def __init__(self, dataname):
        DataScore.__init__(self, dataname)
    def calcScore(self):
        snow = DataScore.datalist['snow']
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
        DataScore.score['snow'] = result

class TurnSigScore(DataScore): #turnsignal
    def __init__(self, dataname):
        DataScore.__init__(self, dataname)
    def calcScore(self):
        turnsig = DataScore.datalist['turnsignal']
        result = 0
        if turnsig != 0:
            result = 100
        else:
            result = 0
        DataScore.score['turnsignal'] = result

def initAnalysis():
    global DataScoreList
    DataScoreList.append(SpeedScore('speed'))
    DataScoreList.append(GearScore('gear'))
    DataScoreList.append(RainScore('rain'))
    DataScoreList.append(SnowScore('snow'))
    DataScoreList.append(TurnSigScore('turnsignal'))
    
    
def AnalysisReq():
    global ModuleList #�� ����Ʈ���� �� ȹ�� ����� ��ü�� ����Ǿ��ִ�.
    for md in ModuleList:  #�ϴ� ������ ȹ�� ���� ���� �м��� �ʿ��� �����͸� ��� ȹ���ؿ´�
        if ModuleList[md].isChanged() == True:
            moduledatalist = ModuleList[md].getDataList() #�� ����� �ٲ� ����Ÿ�� ����. �� ��Ҵ� key:������..
            for mdl in moduledatalist: #key�� ���� �� ����� ���� �����Ͽ� ���� list�� update
                DataScore.datalist[mdl] = moduledatalist[mdl] #data�� ������Ʈ �Ѵ�
                #DataScore.datalist ���� �������̱� ������ ���� ó�� ���� data�� ���͵� �˾Ƽ� �߰��ϰ� ������Ʈ �Ѵ�
    #������� data�� ������Ʈ�� ����
    #update�� �����ʹ� datalist�� ������
    #���⼭���� �� �Ǵ� ������ ���ھ� ����
    for dsl in DataScoreList: #list�� ��ϵǾ��ִ� Score��� ��ü�� �� ���鼭 (������ 5��)
        dsl.calcScore()  #������ ����Ѵ�.
    #print DataScore.datalist, 'datalist'
    #print DataScore.score, 'score'
    return


ModuleList = None
DataScoreList = []
initAnalysis()
    

        

        
                
    
    
