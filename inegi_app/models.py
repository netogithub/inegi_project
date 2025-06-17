from django.db import models

# Create your models here.
class Estado(models.Model):
    """Modelo que representa un estado en el sistema INEGI.

    Args:
        cve_ent (CharField): Clave del AGEE (max_length=2).
        nomgeo (CharField): Nombre (max_length=50).
        nom_abrev (CharField): Nombre abreviado (max_length=10).
        pob_total (IntegerField): Población total del estado.
        pob_femenina (IntegerField): Población total femenina.
        pob_masculina (IntegerField): Población total masculina.
        total_viviendas_habitadas (IntegerField): Total de viviendas habitadas.
    """
    cve_ent = models.CharField(max_length=2)
    nomgeo = models.CharField(max_length=50)
    nom_abrev = models.CharField(max_length=10)
    pob_total = models.IntegerField()
    pob_femenina = models.IntegerField()
    pob_masculina = models.IntegerField()
    total_viviendas_habitadas = models.IntegerField()

class Municipio(models.Model):
    """Modelo que representa un estado en el sistema INEGI.

    Args:
        estado (Estado): Modelo Estado.
        cve_mun (CharField): Clave del AGEE (max_length=3).
        nomgeo (CharField): Nombre (max_length=80).
        pob_total (IntegerField): Población total del estado.
        pob_femenina (IntegerField): Población total femenina.
        pob_masculina (IntegerField): Población total masculina.
        total_viviendas_habitadas (IntegerField): Total de viviendas habitadas.
    """
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name='municipios')
    cve_mun = models.CharField(max_length=3)
    nomgeo = models.CharField(max_length=80)
    pob_total = models.IntegerField()
    pob_femenina = models.IntegerField()
    pob_masculina = models.IntegerField()
    total_viviendas_habitadas = models.IntegerField()

class Localidad(models.Model):
    """_summary_

    Args:
        municipio (Municipio): Modelo Municipio.
        cve_loc (CharField): Clave del AGEE (max_length=4).
        nomgeo (CharField): Nombre (max_length=100)
        ambito (CharField): Tipo de ámbito (max_length=10)
        longitud (FloatField): Distancia angular entre el meridiano origen y un punto en la superficie terrestre expresada en unidades decimales.
        latitud (FloatField): Distancia angular entre el ecuador y un punto en la superficie terrestre expresada en unidades decimales.
        altitud (IntegerField): Distancia vertical en metros que existe entre un punto de la superficie terrestre y el nivel del mar.
        pob_total (IntegerField): Población total de la localidad.
        total_viviendas_habitadas (IntegerField): Total de viviendas habitadas.
    """
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='localidades')
    cve_loc = models.CharField(max_length=4)
    nomgeo = models.CharField(max_length=100)
    ambito = models.CharField(max_length=10)
    longitud = models.FloatField()
    latitud = models.FloatField()
    altitud = models.IntegerField()
    pob_total = models.IntegerField()
    total_viviendas_habitadas = models.IntegerField()

class Asentamiento(models.Model):
    """_summary_

    Args:
        localidad (Localidad): Modelo Localidad.
        cve_asen (CharField): Clave del asentamiento humano (max_length=4).
        nom_asen (CharField): Nombre del asentamiento (max_length=255).
        tipo_asen (CharField): Nombre del tipo de asentamiento humano (max_length=30).
    """
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, related_name='asentamientos')
    cve_asen = models.CharField(max_length=4)
    nom_asen = models.CharField(max_length=255)
    tipo_asen = models.CharField(max_length=30)