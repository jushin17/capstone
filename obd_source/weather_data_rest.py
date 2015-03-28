# -*- coding: cp949 -*-
import requests
import time

#현재 appKey 를 발급받지 않았기 때문에 아직은 요청 에러가 난다.

#1초에 한번씩 요청해서 결과 출력
loc_data = {'version': '1', 'centerLat': '1', 'centerLon': '126.976937', 'reqCoordType': 'WGS84GEO', 'resCoordType':  'WGS84GEO', 'radius': '1', 'zoomLevel': '14' }
for i in range(10):
    r = requests.get('https://apis.skplanetx.com/tmap/traffic', params=loc_data)
    time.sleep(1)
    print r.text
