# inegi_app/processors/municipio.py
from .base import BaseINEGIProcessor
from inegi_app.models import Municipio, Estado

class MunicipioProcessor(BaseINEGIProcessor):
    REQUIRED_FIELDS = ['cve_mun', 'nomgeo', 'pob_total', 'pob_femenina', 'pob_masculina', 'total_viviendas_habitadas']

    def process_data(self):
        """Proceso para descargar los municipios por estados de México de la api de INEGI
        """
        estados = Estado.objects.all()
        if not estados.exists():
            self.stdout.write(self.style.WARNING("No hay estados registrados"))
            return

        for estado in estados:
            data = self.request_inegi(f'mgem/{str(estado.cve_ent).rjust(2, "0")}')
            if not data.get('datos'):
                self.stdout.write(self.style.WARNING(f"No hay datos"))
                continue
            for item in data.get('datos', []):
                if not self.validate_data(item, self.REQUIRED_FIELDS):
                    self.stdout.write(self.style.WARNING(f"Municipio incompleto: {item}"))
                    continue

                try:
                    Municipio.objects.update_or_create(
                        estado=estado,
                        cve_mun=item['cve_mun'],
                        defaults={
                            'nomgeo': item['nomgeo'],
                            'pob_total': item['pob_total'],
                            'pob_femenina': item['pob_femenina'],
                            'pob_masculina': item['pob_masculina'],
                            'total_viviendas_habitadas': item['total_viviendas_habitadas'],
                        }
                    )
                    self.stdout.write(f"Municipio {item['nomgeo']} guardado.")
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error al guardar municipio: {e}"))