# -*- coding: cp949 -*-
import requests
from requests.auth import AuthBase

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
#print r.text

#appkey : fba5994b-9c36-3050-8157-e67d96f7b182
