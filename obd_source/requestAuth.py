# -*- coding: cp949 -*-
import requests
from requests.auth import AuthBase

class appAuth(AuthBase):
    """Attaches HTTP Authentication to the given Request object."""
    #requset ��û ��ü�� appkey�� �߰�
    def __init__(self, username):
        # setup any auth-related data here
        self.username = username

    def __call__(self, r):
        # modify and return the request
        r.headers['appKey'] = self.username
        return r


#1�ʿ� �ѹ��� ��û�ؼ� ��� ���
#print r.text

#appkey : fba5994b-9c36-3050-8157-e67d96f7b182
