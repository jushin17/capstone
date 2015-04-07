# -*- coding: cp949 -*-
import time
import threading
import requestAuth
import requests
from time import *
import json

class DataDev(threading.Thread):
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
    
class OBD2(DataDev):
    def __init__(self):
        DataDev.__init__(self)
        self.datalist = {'speed': 0, 'steering': 0, 'gear':0}
        
    def updateData(self, speed=-1, steering=-1, gear=-1):
        if(speed != -1):
            self.datalist['speed'] = speed
        if(steering != -1):
            self.datalist['steering'] = steering
        if(gear != -1):
            self.datalist['gear'] = gear
        return
        
class Weather(DataDev):
    lat = 0
    lon = 0
    def __init__(self):
        self.weather_data = {'version':'1','lat': '37.596187', 'lon': '126.953547'}
        DataDev.__init__(self)
        self.datalist = {'rain': 0, 'snow':0}

    def updateData(self):
        return
    
    def updatelatlon(self, lat, lon):
        Weather.lat = lat
        Weather.lon = lon

    def run(self):
        while True:
            self.weather_data['lat'] = Weather.lat
            self.weather_data['lon'] = Weather.lon
            r = requests.get('http://apis.skplanetx.com/weather/current/minutely', auth=requestAuth.appAuth('fba5994b-9c36-3050-8157-e67d96f7b182'),params=self.weather_data)
            j = json.loads(r.text)
            print j['weather']['minutely'][0]['sky']['name']
            sleep(3)
        
class Road(DataDev):
    lat = 0
    lon = 0
    def __init__(self):
        self.loc_data = {'version': '1', 'centerLat': '37.596187', 'centerLon': '126.953547', 'reqCoordType': 'WGS84GEO', 'resCoordType':  'WGS84GEO', 'radius': '1', 'zoomLevel': '11', 'trafficType': 'AROUND'}
        DataDev.__init__(self)
        self.datalist = {'roadtype': 0}

    def updatelatlon(self, lat, lon):
        Road.lat = lat
        Road.lon = lon

    def updateData(self):
        return

    def run(self):
        while True:
            print 'Road lat : ', Road.lat, ' lon : ', Road.lon
            self.loc_data['centerLat'] = Road.lat
            self.loc_data['centerLon'] = Road.lon
            r = requests.get('https://apis.skplanetx.com/tmap/traffic', auth=requestAuth.appAuth('fba5994b-9c36-3050-8157-e67d96f7b182'),params=self.loc_data)
            j = json.loads(r.text)
            print j['features'][0]['properties']['description']
            sleep(3)
            
def getModuleList():
    global moduleList
    return moduleList


