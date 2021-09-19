import requests
import json
from pathlib import Path

# Gets your currentt ipv4 / ipv6 address
class _ipify():
    apiAddress = "https://api64.ipify.org"

    def __init__(self, ca=None, requestTimeout=15):
        self.requestTimeout = requestTimeout
        if ca != None:
            if type(ca) is str:
                self.ca = str(Path(ca))
            elif type(ca) is bool:
                self.ca = ca
        else:
            self.ca = None

    def apiCall(self,endpoint,methord="GET",data=None):
        kwargs={}
        kwargs["timeout"] = self.requestTimeout
        if self.ca != None:
            kwargs["verify"] = self.ca
        try:
            url = "{0}/{1}".format(self.apiAddress,endpoint)
            if methord == "GET":
                response = requests.get(url, **kwargs)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            return 0, "Connection Timeout - {0}".format(e)
        return response.status_code, json.loads(response.text)

    def getMyIPAddress(self):
        statusCode, response = self.apiCall("?format=json")
        if statusCode == 200:
            return response["ip"]
        return None

# Gets IP Geo Infomation
class _geoipify():
    apiAddress = "https://geo.ipify.org/api/v1"

    def __init__(self, apiToken, ca=None, requestTimeout=15):
        self.apiToken = apiToken
        self.requestTimeout = requestTimeout
        if ca != None:
            if type(ca) is str:
                self.ca = str(Path(ca))
            elif type(ca) is bool:
                self.ca = ca
        else:
            self.ca = None

    def apiCall(self,endpoint,methord="GET",data=None):
        kwargs={}
        kwargs["timeout"] = self.requestTimeout
        if self.ca != None:
            kwargs["verify"] = self.ca
        try:
            url = "{0}?apiKey={1}&{2}".format(self.apiAddress,self.apiToken,endpoint)
            if methord == "GET":
                response = requests.get(url, **kwargs)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            return 0, "Connection Timeout - {0}".format(e)
        return response.status_code, json.loads(response.text)

    def geoIPLookup(self,ip):
        statusCode, response = self.apiCall("ipAddress={0}".format(ip))
        return statusCode, response

# Detects proxy, vpn / tor addresses from ip
class _proxyipify():
    apiAddress = "https://vpn-proxy-detection.ipify.org/api/v1"

    def __init__(self, apiToken, ca=None, requestTimeout=15):
        self.apiToken = apiToken
        self.requestTimeout = requestTimeout
        if ca != None:
            if type(ca) is str:
                self.ca = str(Path(ca))
            elif type(ca) is bool:
                self.ca = ca
        else:
            self.ca = None

    def apiCall(self,endpoint,methord="GET",data=None):
        kwargs={}
        kwargs["timeout"] = self.requestTimeout
        if self.ca != None:
            kwargs["verify"] = self.ca
        try:
            url = "{0}?apiKey={1}&{2}".format(self.apiAddress,self.apiToken,endpoint)
            if methord == "GET":
                response = requests.get(url, **kwargs)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            return 0, "Connection Timeout - {0}".format(e)
        return response.status_code, json.loads(response.text)

    def proxyDetect(self,ip):
        statusCode, response = self.apiCall("ipAddress={0}".format(ip))
        return statusCode, response
