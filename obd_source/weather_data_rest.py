# -*- coding: cp949 -*-
import requests
import time

#���� appKey �� �߱޹��� �ʾұ� ������ ������ ��û ������ ����.

#1�ʿ� �ѹ��� ��û�ؼ� ��� ���
loc_data = {'version': '1', 'centerLat': '1', 'centerLon': '126.976937', 'reqCoordType': 'WGS84GEO', 'resCoordType':  'WGS84GEO', 'radius': '1', 'zoomLevel': '14' }
for i in range(10):
    r = requests.get('https://apis.skplanetx.com/tmap/traffic', params=loc_data)
    time.sleep(1)
    print r.text
