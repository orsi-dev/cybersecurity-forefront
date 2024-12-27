# Desc: Healthcheck handler for the REST API
import logging
import os

from sanic import json

from src.config.forefront_metadata import InfoFusionMetadata


class HealthCheckHandler:
    def __init__(self, service):
        self.service = service # Dependency Injection
        self.logger = logging.getLogger(self.__class__.__name__)
    
    async def post(self):
        return None, 405
    
    async def get(self, request):
        self.logger.info("Fetching healthcheck status...")
        health_status = await self.service.get_health()
        self.logger.info("Healthcheck status fetched successfully")
        return json(health_status, status=200)

