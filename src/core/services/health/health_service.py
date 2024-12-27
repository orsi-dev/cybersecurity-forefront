import datetime
import os
from src.config.forefront_metadata import ForefrontMetadata


class HealthService:
    def __init__(self):
        pass

    async def get_health(self):
        app_version = ForefrontMetadata().get_version()       
        return {
            "app": os.getenv("APP_NAME", "ForeFront"),
            "version": app_version if app_version else "unknown",
            "status": "ok",
            "timestamp": datetime.datetime.now().isoformat(),
            
            }, 200
    
    async def get_health_details(self):
        '''
        Return a detailed healthcheck
        '''
        return {
            "status": "ok",
            "timestamp": datetime.now().isoformat(),
            "services": {
                "db": "ok", #TODO: implement
                "storage": "ok", #TODO: implement
                "queue": "ok", #TODO: implement
                "cache": "ok", #TODO: implement
            },
            "system": {
                "os": "Linux", #TODO: implement
                "disk_space": "TODO", #TODO: implement
                "cpu": "TODO", #TODO: implement
                "memory": "TODO", #TODO: implement
            },
            "app": {
                "version": ForefrontMetadata().get_version() if ForefrontMetadata().get_version() else "unknown",
                "name": os.getenv("APP_NAME", "ForeFront"),
                "description": "TODO", #TODO: implement
                "dependencies": "TODO", #TODO: implement
            },
            "metadata": {
                "author": "TODO", #TODO: implement
                "company": "TODO", #TODO: implement
                "license": "TODO", #TODO: implement
                "repository": "TODO", #TODO: implement
            },
            "links": {
                "self": "TODO", #TODO: implement
                "documentation": "TODO", #TODO: implement
            }
        }, 200