# inegi_app/management/commands/populate_inegi.py
from django.core.management.base import BaseCommand
from inegi_app.processors.estado import EstadoProcessor
from inegi_app.processors.municipio import MunicipioProcessor
from inegi_app.processors.localidad import LocalidadProcessor
from inegi_app.processors.asentamiento import AsentamientoProcessor

class Command(BaseCommand):
    help = 'Importa datos del API INEGI a la base de datos'

    def handle(self, *args, **kwargs):
        """_summary_"""
        localidades_limite = kwargs.get('localidades_limite', 10)  # ← Límite predeterminado: 50
        asentamientos_limite = kwargs.get('localidades_limite', 5)
        processors = [
            EstadoProcessor(stdout=self.stdout, style=self.style),
            MunicipioProcessor(stdout=self.stdout, style=self.style),
            LocalidadProcessor(stdout=self.stdout, style=self.style),
            AsentamientoProcessor(stdout=self.stdout, style=self.style),
        ]

        for processor in processors:
            self.stdout.write(self.style.SUCCESS(f"Procesando {processor.__class__.__name__}..."))
            # processor.process_data()
            if isinstance(processor, LocalidadProcessor):
                # Ejecuta con límite personalizado solo para LocalidadProcessor
                processor.process_data(limite=localidades_limite)
            elif isinstance(processor, AsentamientoProcessor):
                processor.process_data(limite=asentamientos_limite)
            else:
                # Ejecuta sin límite para otros procesadores
                processor.process_data()