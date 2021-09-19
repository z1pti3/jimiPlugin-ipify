import jimi

class _ipify(jimi.plugin._plugin):
    version = 0.1

    def install(self):
        # Register models
        jimi.model.registerModel("ipifyGetMyIP","_ipifyGetMyIP","_action","plugins.ipify.models.action")
        jimi.model.registerModel("ipifyGeoIPLookup","_ipifyGeoIPLookup","_action","plugins.ipify.models.action")
        jimi.model.registerModel("ipifyIsIPProxy","_ipifyIsIPProxy","_action","plugins.ipify.models.action")
        return True

    def uninstall(self):
        # deregister models
        jimi.model.deregisterModel("ipifyGetMyIP","_ipifyGetMyIP","_action","plugins.ipify.models.action")
        jimi.model.deregisterModel("ipifyGeoIPLookup","_ipifyGeoIPLookup","_action","plugins.ipify.models.action")
        jimi.model.deregisterModel("ipifyIsIPProxy","_ipifyIsIPProxy","_action","plugins.ipify.models.action")
        return True

    def upgrade(self,LatestPluginVersion):
        #if self.version < 0.2:
        return True
