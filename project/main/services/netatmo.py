import os
from pprint import pprint
import requests
from main.utils.utils import get_random_string, Device, DashboardData, update_ago, health_index_state_color, wifi_status, id_format
import time
import urllib.parse, urllib.request
import json
from ..credentials import credentials


#This class is to manage the Netatmo API 
class Netatmo_Client:
    def __init__(self):
        self.client_id = credentials.client_id
        self.client_secret = credentials.client_secret
        self.token = None
        self.refresh_token = None
        self.expires_in = None
        self.data = None
        self.redirect_uri = os.getenv('HOST_NAME')+'/autorize'



    def login(self):
        payload = {
        'client_id': self.client_id,
        'redirect_uri': self.redirect_uri,
        'scope': 'read_homecoach',
        "state": get_random_string(),
        }

        headers = {}
        return requests.post('https://api.netatmo.com/oauth2/authorize', headers=headers, params=payload).url

    
    def access_token(self, code):
        
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded;chartset=UTF-8'}

        params = {
            'code': code,
            'grant_type': 'authorization_code',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_uri,
            'scope': 'read_homecoach',
            }

        response = requests.post('https://api.netatmo.com/oauth2/token', headers=headers, data=params)

        rjson = response.json()
        self.access_token_ = rjson['access_token']
        self.refresh_token = rjson['refresh_token']
        self.expires_in = int(rjson['expires_in'] + time.time())
        
        

        return rjson


    def refresh_token(self):
        if self.expires_in < time.time(): # Token should be renewed
            print("token should be renewed")
            postParams = {
                    "grant_type" : "refresh_token",
                    "refresh_token" : self.refresh_token,
                    "client_id" : self.client_id,
                    "client_secret" : self.client_secret}


            def postRequest(url, params):
                req = urllib.request.Request(url)
                req.add_header("Content-Type","application/x-www-form-urlencoded;charset=utf-8")
                params = urllib.parse.urlencode(params)
                resp = urllib.request.urlopen(req, params).read()

                return json.loads(resp)

            resp = postRequest('https://api.netatmo.com/oauth2/token', postParams)
            self.access_token = resp['access_token']
            self.refresh_token = resp['refresh_token']
            self.expiration = int(resp['expire_in'] + time.time())

            print(self.access_token)
        return self.access_token


    def get_data(self, token):
        """si funciona"""
        
        headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer '+ token,

        }

        response = requests.get('https://api.netatmo.com/api/gethomecoachsdata', headers=headers,)
        rjson = response.json()
        self.data = rjson

        return rjson

    #deserialize json to object
    def deserialize_devices(self, j):
        pprint(j)
        devices = []
        for device in j:
            pprint(device)
            dashboardata = DashboardData(json.dumps(device['dashboard_data']))
            deviceObj = Device(json.dumps(device))
            deviceObj.dashboard_data = dashboardata

            deviceObj.id = deviceObj._id
            deviceObj.id_front = id_format(deviceObj.id)
            deviceObj.last_status_store = update_ago(deviceObj.last_status_store)
            deviceObj.health_state, deviceObj.health_color = health_index_state_color(deviceObj.dashboard_data.health_idx)
            deviceObj.wifi_message, deviceObj.wifi_idx, deviceObj.wifi_color = wifi_status(deviceObj.wifi_status)

            devices.append(deviceObj)
            print(vars(deviceObj))
            print(vars(deviceObj.dashboard_data))
        return devices













