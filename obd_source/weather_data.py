from httplib import HTTP

request = HTTP('apis.skplanetx.com')
url = '/tmap/traffic?centerLon=126.976937&centerLat=37.575432&version=1&trafficType=AROUND&reqCoordType=WGS84GEO&zoomLevel=14&radius=1&resCoordType=WGS84GEO'
request.putrequest('GET', url)

request.putheader('x-skpop-userId','game2k')
request.putheader('Accept-Language','ko_KR')
request.putheader('Accept', 'application/json')
request.putheader('access_token','')
#request.putheader('appKey','')
request.putheader('Host', 'apis.skplanetx.com')
request.endheaders()

errorCode, errorMessage, headers = request.getreply()
print errorCode, errorMessage

fobj = request.getfile()
html = fobj.read()
fobj.close()
print html
#"GET /


