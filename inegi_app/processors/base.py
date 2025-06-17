# inegi_app/processors/base.py
import requests
import time
import json
from django.core.management.base import BaseCommand
from django.db import transaction

class BaseINEGIProcessor:
    API_URL = 'https://gaia.inegi.org.mx/wscatgeo/v2' 
    
    def __init__(self, stdout=None, style=None):
        self.stdout = stdout
        self.style = style

    def request_inegi(self, endpoint):
        """Solicita datos al API de INEGI"""
        url = f"{self.API_URL}/{endpoint}"
        try:
            response = requests.get(url, timeout=10, verify=False)
            response.raise_for_status()
            time.sleep(1)
            return response.json()
        except requests.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Error de conexión: {e}'))
            return {}

    def validate_data(self, data, required_fields):
        """Valida que existan todos los campos requeridos"""
        for field in required_fields:
            if data.get(field) is None:
                return False
        return True

    @transaction.atomic
    def process_data(self, data):
        raise NotImplementedError("Debe implementar process_data en subclases")