# inegi_app/processors/estado.py
from .base import BaseINEGIProcessor
from inegi_app.models import Estado

class EstadoProcessor(BaseINEGIProcessor):
    REQUIRED_FIELDS = ['cve_ent', 'nomgeo', 'nom_abrev', 'pob_total', 'pob_femenina', 'pob_masculina', 'total_viviendas_habitadas']
    
    def process_data(self):
        """Proceso para descargar los estados de México de al api de INEGI"""
        data = self.request_inegi('mgee/')
        if not data.get('datos'):
            self.stdout.write(self.style.WARNING(f"No hay datos"))
            return
        for item in data.get('datos', []):
            if not self.validate_data(item, self.REQUIRED_FIELDS):
                self.stdout.write(self.style.WARNING(f'Estado incompleto: {item}'))
                continue

            try:
                Estado.objects.update_or_create(
                    cve_ent=item['cve_ent'],
                    defaults={
                        'nomgeo': item['nomgeo'],
                        'nom_abrev': item['nom_abrev'],
                        'pob_total': item['pob_total'],
                        'pob_femenina': item['pob_femenina'],
                        'pob_masculina': item['pob_masculina'],
                        'total_viviendas_habitadas': item['total_viviendas_habitadas'],
                    }
                )
                self.stdout.write(f"Estado {item['nomgeo']} guardado.")
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error al guardar estado: {e}"))