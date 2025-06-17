# inegi_app/processors/localidad.py
from .base import BaseINEGIProcessor
from inegi_app.models import Localidad, Municipio, Estado

class LocalidadProcessor(BaseINEGIProcessor):
    REQUIRED_FIELDS = ['cve_loc', 'nomgeo', 'ambito', 'latitud', 'longitud', 'altitud', 'pob_total', 'total_viviendas_habitadas']

    def process_data(self, limite=10):
        estados = Estado.objects.all()
        if not estados.exists():
            self.stdout.write(self.style.WARNING("No hay estados registrados"))
            return

        for estado in estados:
            municipios = Municipio.objects.filter(estado=estado)
            if not municipios.exists():
                continue

            for municipio in municipios:
                localidad_limite = limite  # ← Límite por municipio
                self.stdout.write(f"Procesando localidades del municipio {municipio.nomgeo} (Límite: {localidad_limite})")

                data = self.request_inegi(f'localidades/{str(estado.cve_ent).rjust(2, "0")}/{str(municipio.cve_mun).rjust(3, "0")}')
                if not data.get('datos'):
                    self.stdout.write(self.style.WARNING(f"No hay datos"))
                    continue
                for item in data.get('datos', []):
                    if localidad_limite <= 0:
                        self.stdout.write(self.style.NOTICE(f"Límite de localidades alcanzado para {municipio.nomgeo}."))
                        break  # ← Salir del bucle de localidades si se alcanza el límite
                    if not self.validate_data(item, self.REQUIRED_FIELDS):
                        self.stdout.write(self.style.WARNING(f"Localidad incompleta: {item}"))
                        continue

                    try:
                        Localidad.objects.update_or_create(
                            municipio=municipio,
                            cve_loc=item['cve_loc'],
                            defaults={
                                'nomgeo': item['nomgeo'],
                                'ambito': item['ambito'],
                                'latitud': item['latitud'],
                                'longitud': item['longitud'],
                                'altitud': item['altitud'],
                                'pob_total': item['pob_total'],
                                'total_viviendas_habitadas': item['total_viviendas_habitadas'],
                            }
                        )
                        self.stdout.write(f"Localidad {item['nomgeo']} guardada.")
                        localidad_limite -= 1  # ← Reduce el límite
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f"Error al guardar localidad: {e}"))