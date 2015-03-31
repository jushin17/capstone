# -*- coding: cp949 -*-

import dataGetModule

class DataScore:
    datalist = {} #class member�� ����
    dataScore = {'speed': 0, 'turnsignal': 0, 'rain': 0, 'snow':0 ,'gear':0}
    def __init__(self, dataname):  #datalist �� Dict���̴�
        DataScore.datalist[dataname] = 0
        
    def initScore(self):
        for dl in DataScore.datalist:
            DataScore.datalist[dl] = 0
            
    def getScore(self, dataname):
            if dataname in DataScore.datalist
                return DataScore.datalist[dataname]
            else
                return -1
            
    def setScore(self, dataname, data):
        if dataname in DataScore.datalist
            DataScore.datalist[dataname] = data
            
    def calcScore(self):
        pass
    


class SpeedScore(DataScore): #speed
    def __init__(self, dataname):
        DataScore.__init__(self, dataname)
    def calcScore(self):
        return DataScore.datalist['speed']
    

class GearScore(DataScore): #gear
    def __init__(self, dataname):    #driveMode ó���� ���� ����ϰ� �����غ���
        DataScore.__init__(self, dataname)
    def calcScore(self):
        gear = DataScore.datalist['gear']
        driveMode = {'parking' : 0, 'dirve': 1, 'back': 2}
        if gear == driveMode['parking']:
            return 0
        elif gear == driveMode['drive']:
            return 20
        elif gear == driveMode['back']:
            return 100
        else:
            return -1

        
class RainScore(DataScore): #rain
    def __init__(self, dataname):
        DataScore.__init__(self, dataname)
    def calcScore(self):
        rain = DataScore.datalist['rain']
        if 0 <= rain <= 5:
            return 10
        elif rain <= 20:
            return 40
        elif rain <= 80:
            return 60
        elif rain > 80:
            return 100
        else:
            return -1

class SnowScore(DataScore): #snow
    def __init__(self, dataname):
        DataScore.__init__(self, dataname)
    def calcScore(self):
        snow = DataScore.datalist['snow']
        if 0 <= snow <= 1:
            return 10
        elif snow <= 5:
            return 40
        elif snow <= 20:
            return 60
        elif snow > 20:
            return 100
        else:
            return -1

class TurnSigScore(DataScore): #turnsignal
    def __init__(self, dataname):
        DataScore.__init__(self, dataname)
    def calcScore(self):
        turnsig = DataScore.datalist['turnsignal']
        if turnsig != 0:
            return 100
        else:
            return 0

def initAnalysis():
    global DataScoreList
    DataScoreList.append(SpeedScore('speed'))
    DataScoreList.append(GearScore('gear'))
    DataScoreList.append(RainScore('rain'))
    DataScoreList.append(SnowScore('snow'))
    DataScoreList.append(TurnSigScore('turnsignal'))
    
    
def AnalysisReq():
    global ModuleList
    for md in ModuleList:  #�ϴ� ������ ȹ�� ���� ���� �м��� �ʿ��� �����͸� ��� ȹ���ؿ´�
        if md.isChanged() == True:
            moduledatalist = md.getDataList() #�� ����� �����ϴ� ����Ÿ ����Ʈ�� ���� ����Ʈ�� �� ��Ҵ� key:������..
            for mdl in moduledatalist: #�� ����Ʈ�� �����ִ� �� �����͸� ���κ��� �о�ͼ� data�� ����
                DataScore.datalist[mdl] = modueldatalist[mdl] #data�� ������Ʈ �Ѵ�
    #������� data�� ������Ʈ�� ����
    #update�� �����ʹ� datalist�� ������

                   
    #���⼭���� �� �Ǵ� ������ ���ھ� ����
    for dsl in DataScoreList: #list�� ��ϵǾ��ִ� Score��� ��ü�� �� ���鼭
        dsl.calcScore()  #������ ����Ѵ�.

    return


ModuleList = ['obd2', 'weather', 'road']
DataScoreList = []

initAnalysis()
    

        

        
                
    
    
