# -*- coding: cp949 -*-

import dataGetModule

class DataScore:
    datalist = {} #class member로 선언
    score = {'speed': 0, 'steering': 0, 'rain': 0, 'snow':0 ,'gear':0}
    def __init__(self, dataname):  #datalist 는 Dict형이다
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
    def __init__(self, dataname):    #driveMode 처리를 좀더 깔끔하게 생각해보기
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

class SteeringScore(DataScore): #turnsignal
    def __init__(self, dataname):
        DataScore.__init__(self, dataname)
    def calcScore(self):
        turnsig = DataScore.datalist['steering']
        result = 0
        if turnsig != 0:
            result = 100
        else:
            result = 0
        DataScore.score['steering'] = result

def initAnalysis():
    global DataScoreList
    DataScoreList.append(SpeedScore('speed'))
    DataScoreList.append(GearScore('gear'))
    DataScoreList.append(RainScore('rain'))
    DataScoreList.append(SnowScore('snow'))
    DataScoreList.append(SteeringScore('steering'))
    
    
def AnalysisReq():
    global DataGetList #이 리스트에는 각 획득 모듈의 객체가 저장되어있다.
    for md in DataGetList:  #일단 각각의 획득 모듈로 부터 분석에 필요한 데이터를 모두 획득해온다
        if DataGetList[md].isChanged() == True:
            moduledatalist = DataGetList[md].getSensorList() #각 모듈의 바뀐 데이타를 얻어옴. 각 요소는 key:값으로..
            for mdl in moduledatalist: #key를 통해 각 요소의 값에 접근하여 이쪽 list에 update
                DataScore.datalist[mdl] = moduledatalist[mdl] #data를 업데이트 한다
                #DataScore.datalist 또한 사전형이기 때문에 만약 처음 보는 data가 들어와도 알아서 추가하고 업데이트 한다
    #여기까지 data의 업데이트가 끝남
    #update된 데이터는 datalist에 들어가있음
    #여기서부터 각 판단 기준의 스코어 산정
    for dsl in DataScoreList: #list에 등록되어있는 Score계산 객체를 쭉 돌면서 (지금은 5개)
        dsl.calcScore()  #점수를 계산한다.
    #print DataScore.datalist, 'datalist'
    #print DataScore.score, 'score'
    return

DataGetList = None
DataScoreList = []
initAnalysis()
    

        

        
                
    
    
