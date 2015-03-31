# -*- coding: cp949 -*-

import dataGetModule

class DataScore:
    datalist = {} #class member로 선언
    dataScore = {'speed': 0, 'turnsignal': 0, 'rain': 0, 'snow':0 ,'gear':0}
    def __init__(self, dataname):  #datalist 는 Dict형이다
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
    def __init__(self, dataname):    #driveMode 처리를 좀더 깔끔하게 생각해보기
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
    for md in ModuleList:  #일단 각각의 획득 모듈로 부터 분석에 필요한 데이터를 모두 획득해온다
        if md.isChanged() == True:
            moduledatalist = md.getDataList() #각 모듈이 관리하는 데이타 리스트를 얻어옴 리스트의 각 요소는 key:값으로..
            for mdl in moduledatalist: #그 리스트에 속해있는 각 데이터를 모듈로부터 읽어와서 data에 저장
                DataScore.datalist[mdl] = modueldatalist[mdl] #data를 업데이트 한다
    #여기까지 data의 업데이트가 끝남
    #update된 데이터는 datalist에 들어가있음

                   
    #여기서부터 각 판단 기준의 스코어 산정
    for dsl in DataScoreList: #list에 등록되어있는 Score계산 객체를 쭉 돌면서
        dsl.calcScore()  #점수를 계산한다.

    return


ModuleList = ['obd2', 'weather', 'road']
DataScoreList = []

initAnalysis()
    

        

        
                
    
    
