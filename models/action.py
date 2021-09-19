import jimi

from plugins.ipify.includes import ipify

class _ipifyGetMyIP(jimi.action._action):

    def doAction(self,data):
        response = ipify._ipify().getMyIPAddress()
        if response:
            return { "result" : True, "rc" : 200, "ip" : response }
        else:
            return { "result" : False, "rc" : 404, "msg" : "Failed to get a valid response from API call" }

class _ipifyGeoIPLookup(jimi.action._action):
    ip = str()
    apiToken = str()

    def doAction(self,data):
        ip = jimi.helpers.evalString(self.ip,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        if self.apiToken.startswith("ENC") and self.apiToken != "":
            apiToken = jimi.auth.getPasswordFromENC(self.apiToken)
        statusCode, response = ipify._geoipify(apiToken).geoIPLookup(ip)
        return { "result" : True, "rc" : statusCode, "response" : response }

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiToken" and not value.startswith("ENC "):
            self.apiToken = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
            return True
        return super(_ipifyGeoIPLookup, self).setAttribute(attr,value,sessionData=sessionData)

class _ipifyIsIPProxy(jimi.action._action):
    ip = str()
    apiToken = str()

    def doAction(self,data):
        ip = jimi.helpers.evalString(self.ip,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        if self.apiToken.startswith("ENC") and self.apiToken != "":
            apiToken = jimi.auth.getPasswordFromENC(self.apiToken)
        statusCode, response = ipify._proxyipify(apiToken).proxyDetect(ip)
        return { "result" : True, "rc" : statusCode, "response" : response }

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiToken" and not value.startswith("ENC "):
            self.apiToken = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
            return True
        return super(_ipifyIsIPProxy, self).setAttribute(attr,value,sessionData=sessionData)