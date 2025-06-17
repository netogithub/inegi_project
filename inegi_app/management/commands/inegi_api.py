# inegi_app/management/commands/populate_inegi.py
from django.core.management.base import BaseCommand
from inegi_app.processors.estado import EstadoProcessor
from inegi_app.processors.municipio import MunicipioProcessor
from inegi_app.processors.localidad import LocalidadProcessor
from inegi_app.processors.asentamiento import AsentamientoProcessor

class Command(BaseCommand):
    help = 'Importa datos del API INEGI a la base de datos'

    def add_arguments(self, parser):
        parser.add_argument(
            '--limite',
            type=int,
            default=10,
            help='Número máximo de localidades y asentamientos a procesar por municipio'
        )
        parser.add_argument(
            '--no-limite',
            action='store_true',
            help='Procesa de localidades y asentamientos sin límite'
        )
    

    def handle(self, *args, **kwargs):
        """Funcion que procesa la descarga de elmentos de la API de INEGI"""

        limite = kwargs.get('limite', 10)  # ← Límite predeterminado: 10
        if limite <= 0:
            self.stdout.write(self.style.ERROR("El límite debe ser mayor a 0"))
            return
        if kwargs.get('no_limite'):
            limite = float('inf')  # Procesa todas las localidades
        
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
                processor.process_data(limite)
            elif isinstance(processor, AsentamientoProcessor):
                # Ejecuta con límite personalizado solo para AsentamientoProcessor
                processor.process_data(limite)
            else:
                # Ejecuta sin límite para otros procesadores
                processor.process_data()