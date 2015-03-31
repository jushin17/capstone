# -*- coding: cp949 -*-

import dataGetModule

ModuleList = ['obd2', 'weather', 'road']
data = { 'speed' : 0, 'roadtype': 0, 'rain': 0, 'snow': 0, 'gear': 0} #speed�� ���� �״�� �����̸� ���� ��ü�� ��� key�� ������� �ڵ����� key�� �������ش�
dataScore = {'speed': 0, 'turnsignal': 0, 'rain': 0, 'snow':0 ,'gear':0}
driveMode = {'parking' : 0, 'dirve': 1, 'back': 2}

calcFunc = {'speed': calcSpedScore, 'gear': calcGearScore, 'turnsignal': calcTurnSigScore, 'rain': calcRainScore, 'snow': calcSnowScore}
def AnalysisReq():
    for md in ModuleList:
        if md.isChanged():
            datalist = md.getDataList() #�� ����� �����ϴ� ����Ÿ ����Ʈ�� ���� ����Ʈ�� �� ��Ҵ� ��Ʈ��
            for dl in datalist: #�� ����Ʈ�� �����ִ� �� �����͸� ���κ��� �о�ͼ� data�� ����
                data[dl] = md.getData(dl) #data�� ������Ʈ �Ѵ�
    #������� data�� ������Ʈ�� ����
    #���⼭���� �� �Ǵ� ������ ���ھ� ����
    for key in calcFunc:
        dataScore[key] = calcFunc[key](data[key])
        

def calcSpeedScore(speed): #�ϴ��� ���밪 ���ھ� & Linear Score
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
    
    

        

        
                
    
    
