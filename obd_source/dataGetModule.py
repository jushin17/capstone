# -*- coding: cp949 -*-
import time
import threading
import requests
from time import *
import json
import DataStore
from DataStore import CDataStore
import programOption

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

    def run(self):
        while self.running:
            CGetWeatherData.weather_data['lat'] = CDataStore.SensorData['lat']
            CGetWeatherData.weather_data['lon'] = CDataStore.SensorData['lon']
            r = requests.get('http://apis.skplanetx.com/weather/current/minutely', auth=requestAuth.appAuth('fba5994b-9c36-3050-8157-e67d96f7b182'),params=CGetWeatherData.weather_data)
            j = json.loads(r.text)
            #print j
            print j['weather']['minutely'][0]['sky']['name']
            CDataStore.SensorData['weather'] = j['weather']['minutely'][0]['sky']['name']
            sleep(3)
        print 'stop GetWeatherData'
        
class CGetRoadData(CGetData):
    loc_data = {'version': '1', 'centerLat': '37.596187', 'centerLon': '126.953547', 'reqCoordType': 'WGS84GEO', 'resCoordType':  'WGS84GEO', 'radius': '1', 'zoomLevel': '11', 'trafficType': 'AROUND'}
    def __init__(self):
        CGetData.__init__(self)

    def run(self):
        while self.running:
            #print 'Road lat : ', Road.lat, ' lon : ', Road.lon
            CGetRoadData.loc_data['centerLat'] = CDataStore.SensorData['lat']
            CGetRoadData.loc_data['centerLon'] = CDataStore.SensorData['lon']
            r = requests.get('https://apis.skplanetx.com/tmap/traffic', auth=requestAuth.appAuth('fba5994b-9c36-3050-8157-e67d96f7b182'),params=CGetRoadData.loc_data)
            j = json.loads(r.text)
            #print r.text
            print j['features'][0]['properties']['description']
            CDataStore.SensorData['weather'] = j['features'][0]['properties']['description']
            
            sleep(5)
        print 'stop GetRoadData'



class GpsPoller(CGetData):
    def __init__(self):
        CGetData.__init__(self)
        if programOption.mode != programOption.TESTMODE:
            global gpsd #bring it in scope
            gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
 
    def run(self):
        global gpsd
        if programOption.mode == programOption.TESTMODE:
            gpsfile = file('testgps.txt')
            line = gpsfile.readline()
            while line and self.running:
                print self.running
                #여기에 gpsd에서 계속 데이터를 읽어오는 코드를 작성
                lst = line.split() #lat, lon
                CDataStore.SensorData['lat'] = lst[0]
                CDataStore.SensorData['lon'] = lst[1]


                
                #dataGetList['weather'].updatelatlon(lst[0], lst[1])
                #dataGetList['road'].updatelatlon(lst[0], lst[1])
                sleep(4)
                line = gpsfile.readline()
                print lst[0], lst[1]
        else:
            while self.running:
                gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer
                CDataStore.SensorData['lat'] = gpsd.fix.latitude
                CDataStore.SensorData['lon'] = gpsd.fix.longitude

        print 'stop GpsPoller'


                

class pyOBDReader(CGetData):
    def __init__(self):
        CGetData.__init__(self)
 
    def run(self):
        global mode
        if programOption.mode == programOption.TESTMODE:
            with open('test.json') as f:
                for line in f:
                    if self.running == False:
                        break
                    obdjson = json.loads(line)
                    if(obdjson['name']=='vehicle_speed'):
                        CDataStore.SensorData['speed'] = obdjson['value']
                        #dataGetList['obd2'].updateData(speed = test['value'])
                    elif(obdjson['name']=='transmission_gear_position'):
                        if obdjson['value'] == 'reverse':
                            CDataStore.SensorData['gear'] = obdjson['value']
                            #/////////////////////////////////////////////////////////////////////////
                            #reverse 이외의 데이터도 처리 코드 추가
                            #dataGetList['obd2'].updateData(gear = test['value'])                        
                    elif(obdjson['name']=='steering_wheel_angle'):
                        CDataStore.SensorData['steering'] = obdjson['value']
                        #dataGetList['obd2'].updateData(steering = test['value'])
                    sleep(1)
        else:
            pass
        print 'stop pyOBDReader'


