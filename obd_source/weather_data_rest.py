# -*- coding: cp949 -*-
import requests
from requests.auth import AuthBase
import time


loc_data = {'version': '1', 'centerLat': '37.596187', 'centerLon': '126.953547', 'reqCoordType': 'WGS84GEO', 'resCoordType':  'WGS84GEO', 'radius': '1', 'zoomLevel': '11', 'trafficType': 'AROUND'}
weather_data = {'version':'1','lat': '37.596187', 'lon': '126.953547'}

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


#1초에 한번씩 요청해서 결과 출력
#requests.headers['appKey'] = 'f110d73f-bd4a-33f6-89fd-aa6076ce3cec'

if __name__ == '__main__':

    while True:
        r = requests.get('http://apis.skplanetx.com/weather/current/minutely', auth=appAuth('fba5994b-9c36-3050-8157-e67d96f7b182'),params=weather_data)
        print r.text        
        r = requests.get('https://apis.skplanetx.com/tmap/traffic', auth=appAuth('fba5994b-9c36-3050-8157-e67d96f7b182'),params=loc_data)
        print r.text        
        time.sleep(1)


#print r.text

#appkey : 'f110d73f-bd4a-33f6-89fd-aa6076ce3cec'
