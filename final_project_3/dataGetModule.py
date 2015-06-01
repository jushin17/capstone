# -*- coding: cp949 -*-
import time
import threading
import requests
from time import *
import json
import DataStore
from DataStore import CDataStore
import programOption
from requests.auth import AuthBase
import obd_recorder


gpsd = None

class appAuth(AuthBase):
    """Attaches HTTP Authentication to the given Request object."""
    #requset 요청 객체에 appkey를 추가
    def __init__(self, username):
        # setup any auth-related data here
        self.username = username

    def __call__(self, r):
        # modify and return the request
        r.headers['appKey'] = self.username
        return r

class CGetData(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.current_value = None
        self.running = True
        return

    def getSensorList(self):
        return self.datalist
    def isChanged(self): #일단 무조건 True로 returns
        return True

    def updateData(self):
        return

    def run(self):
        pass
    
        
class CGetWeatherData(CGetData):
    weather_data = {'version':'1','lat': '37.596187', 'lon': '126.953547'}
    def __init__(self):
        CGetData.__init__(self)
        CDataStore.SensorData['rain'] = -1
        CDataStore.SensorData['snow'] = -1

    def run(self):
        while self.running:
            if programOption.mode == programOption.TESTMODE:
                CDataStore.SensorData['rain'] = 0
            else:
                if CDataStore.SensorData['lat'] == -1 or CDataStore.SensorData['lon'] == -1:
                    sleep(2)
                    continue
                CGetWeatherData.weather_data['lat'] = CDataStore.SensorData['lat']
                CGetWeatherData.weather_data['lon'] = CDataStore.SensorData['lon']
                r = requests.get('http://apis.skplanetx.com/weather/current/minutely', auth=appAuth('fba5994b-9c36-3050-8157-e67d96f7b182'),params=CGetWeatherData.weather_data, verify=True)
                j = json.loads(r.text)
                #print float(j['weather']['minutely'][0]['rain']['last10min'])
                if 'error' in j:
                    print "CGetWeatherData error : Data get Fail"
                    break
                else:
                    CDataStore.SensorData['rain'] = float(j['weather']['minutely'][0]['rain']['last10min'])
            sleep(60)
        print 'stop GetWeatherData'


        
class CGetRoadData(CGetData):
    loc_data = {'version': '1', 'centerLat': '37.596187', 'centerLon': '126.953547', 'reqCoordType': 'WGS84GEO', 'resCoordType':  'WGS84GEO', 'radius': '1', 'zoomLevel': '11', 'trafficType': 'AROUND'}
    def __init__(self):
        CGetData.__init__(self)
        CDataStore.SensorData['road'] = -1

    def run(self):
        while self.running:
            if programOption.mode == programOption.TESTMODE:
                CDataStore.SensorData['road'] = 2
            else:
                if CDataStore.SensorData['lat'] == -1 or CDataStore.SensorData['lon'] == -1:
                    sleep(2)
                    continue
                #print 'Road lat : ', Road.lat, ' lon : ', Road.lon
                CGetRoadData.loc_data['centerLat'] = CDataStore.SensorData['lat']
                CGetRoadData.loc_data['centerLon'] = CDataStore.SensorData['lon']
                r = requests.get('https://apis.skplanetx.com/tmap/traffic', auth=appAuth('fba5994b-9c36-3050-8157-e67d96f7b182'),params=CGetRoadData.loc_data, verify=True)
                j = json.loads(r.text)
                #print r.text
                #print int(j['features'][0]['properties']['roadType'])
                #print j['error']
                if 'error' in j:
                    print "CGetRoadData error : Data get Fail"
                    break
                else:
                    CDataStore.SensorData['road'] = int(j['features'][0]['properties']['roadType'])
            sleep(5)
        print 'stop GetRoadData'



class GpsPoller(CGetData):
    def __init__(self):
        CGetData.__init__(self)
        CDataStore.SensorData['lat'] = -1
        CDataStore.SensorData['lon'] = -1
        if programOption.mode == programOption.TESTMODE:
            return
        elif programOption.mode == programOption.EXMODE:
            global gpsd #bring it in scope
            gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
 
    def run(self):
        global gpsd
        if programOption.mode == programOption.TESTMODE:
            while self.running:
                gpsfile = file('testgps.txt')
                line = gpsfile.readline()
                while line and self.running:
                    #print self.running
                    #여기에 gpsd에서 계속 데이터를 읽어오는 코드를 작성
                    lst = line.split() #lat, lon
                    CDataStore.SensorData['lat'] = lst[0]
                    CDataStore.SensorData['lon'] = lst[1]
    
                    #dataGetList['weather'].updatelatlon(lst[0], lst[1])
                    #dataGetList['road'].updatelatlon(lst[0], lst[1])
                    sleep(1)
                    line = gpsfile.readline()
                    #print lst[0], lst[1]
                gpsfile.close()
        elif programOption.mode == programOption.EXMODE:
            while self.running:
                gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer
                CDataStore.SensorData['lat'] = gpsd.fix.latitude
                CDataStore.SensorData['lon'] = gpsd.fix.longitude

        print 'stop GpsPoller'

class pyOBDReader(CGetData):  #test모드 일때는 파일로부터 값을 읽어와야 한다. 즉 모드에 따라 읽어올 대상을 정리하여야 한다
    def __init__(self, filename = "test2.json"):  #객체 생성할 때 불려올거고 준비가 완료되면 리턴한다.
        CGetData.__init__(self)
        CDataStore.SensorData['speed'] = -1
        CDataStore.SensorData['gear'] = -1
        CDataStore.SensorData['steering']  = -1
        self.testfile = filename
        #만약 테스트 모드라면 바로 준비 ok 이면 되고
        if programOption.mode == programOption.TESTMODE:  # 테스트 모드
            return
        elif programOption.mode == programOption.EXMODE: #주행 모드
        #주행모드라면 pyOBD객체에 대한 준비 완료 후 리턴한다
            return  #여기에 pyOBD객체 초기화 코드를 추가
 
    def run(self):
        if programOption.mode == programOption.TESTMODE:
            while self.running:
                with open(self.testfile) as f:
                    for line in f:
                        if self.running == False:
                            break
                        obdjson = json.loads(line)
                        if(obdjson['name']=='vehicle_speed'):
                            CDataStore.SensorData['speed'] = int(obdjson['value'])
                            #dataGetList['obd2'].updateData(speed = test['value'])
                        elif(obdjson['name']=='transmission_gear_position'):
                            if obdjson['value'] == 'reverse':
                                CDataStore.SensorData['gear'] = obdjson['value']
                                #/////////////////////////////////////////////////////////////////////////
                                #reverse 이외의 데이터도 처리 코드 추가
                                #dataGetList['obd2'].updateData(gear = test['value'])                        
                        elif(obdjson['name']=='steering_wheel_angle'):
                            #print abs(abs(-52.699951) - abs(float(obdjson['value'])))
                            #CDataStore.SensorData['steering'] = abs(abs(-52.699951) - abs(float(obdjson['value'])))
                            CDataStore.SensorData['steering'] = abs(float(obdjson['value']))
                            #dataGetList['obd2'].updateData(steering = test['value'])
                        sleep(0.02)
        elif programOption.mode == programOption.EXMODE:
            obd_recoder.obdrecorderstart()
            
        print 'stop pyOBDReader'


