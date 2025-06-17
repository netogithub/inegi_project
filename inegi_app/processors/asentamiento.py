# inegi_app/processors/asentamiento.py
from .base import BaseINEGIProcessor
from inegi_app.models import Asentamiento, Localidad

class AsentamientoProcessor(BaseINEGIProcessor):
    REQUIRED_FIELDS = ['cve_asen', 'nom_asen', 'tipo_asen']
    
    def process_data(self, limite=5):
        localidades = Localidad.objects.all()
        if not localidades.exists():
            self.stdout.write(self.style.WARNING("No hay localidades registradas"))
            return

        for localidad in localidades:
            asentamiento_limite = limite  # ← Límite por localidad
            self.stdout.write(f"Procesando asentamientos de la localidad {localidad.nomgeo} (Límite: {asentamiento_limite})")

            data = self.request_inegi(f"asentamientos/{localidad.municipio.estado.cve_ent}/{localidad.municipio.cve_mun}")
            if not data.get('datos'):
                self.stdout.write(self.style.WARNING(f"No hay datos"))
                continue
            for item in data.get('datos', []):
                if asentamiento_limite <= 0:
                    self.stdout.write(self.style.NOTICE(f"Límite de asentamientos alcanzado para {localidad.nomgeo}."))
                    break  # ← Salir del bucle de localidades si se alcanza el límite
                if not self.validate_data(item, self.REQUIRED_FIELDS):
                    self.stdout.write(self.style.WARNING(f"Asentamiento incompleto: {item}"))
                    continue

                try:
                    Asentamiento.objects.update_or_create(
                        localidad=localidad,
                        cve_asen=item['cve_asen'],
                        defaults={'nom_asen': item['nom_asen'], 'tipo_asen': item['tipo_asen']}
                    )
                    self.stdout.write(f"Asentamiento {item['nom_asen']} guardado.")
                    asentamiento_limite -= 1  # ← Reduce el límite
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error al guardar asentamiento: {e}"))