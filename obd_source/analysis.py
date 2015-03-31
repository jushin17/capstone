# -*- coding: cp949 -*-

import dataGetModule

ModuleList = ['obd2', 'weather', 'road']
data = { 'speed' : 0, 'roadtype': 0, 'rain': 0, 'snow': 0, 'gear': 0} #speed는 거의 그대로 쓸것이며 사전 객체의 경우 key가 없을경우 자동으로 key를 생성해준다
dataScore = {'speed': 0, 'turnsignal': 0, 'rain': 0, 'snow':0 ,'gear':0}
driveMode = {'parking' : 0, 'dirve': 1, 'back': 2}

calcFunc = {'speed': calcSpedScore, 'gear': calcGearScore, 'turnsignal': calcTurnSigScore, 'rain': calcRainScore, 'snow': calcSnowScore}
def AnalysisReq():
    for md in ModuleList:
        if md.isChanged():
            datalist = md.getDataList() #각 모듈이 관리하는 데이타 리스트를 얻어옴 리스트의 각 요소는 스트링
            for dl in datalist: #그 리스트에 속해있는 각 데이터를 모듈로부터 읽어와서 data에 저장
                data[dl] = md.getData(dl) #data를 업데이트 한다
    #여기까지 data의 업데이트가 끝남
    #여기서부터 각 판단 기준의 스코어 산정
    for key in calcFunc:
        dataScore[key] = calcFunc[key](data[key])
        

def calcSpeedScore(speed): #일단은 절대값 스코어 & Linear Score
    return speed
              
def calcGearScore(gear):
    if gear == driveMode['parking']:
        return 0
    elif gear == driveMode['drive']:
        return 20
    elif gear == driveMode['back']:
        return 100
    else:
        return -1

def calcTurnSigScore(turnsig):
    if turnsig != 0:
        return 100
    else:
        return 0

def calcRainScore(rain):
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
    
def calcSnowScore(snow):
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
    
    

        

        
                
    
    
