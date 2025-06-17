from rest_framework import serializers
from .models import Estado, Municipio, Localidad, Asentamiento

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['cve_ent', 'nomgeo', 'pob_total', 'pob_femenina', 'pob_masculina', 'total_viviendas_habitadas']

class MunicipioSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer(read_only=True)

    class Meta:
        model = Municipio
        fields = ['cve_mun', 'nomgeo', 'pob_total', 'pob_femenina', 'pob_masculina', 'total_viviendas_habitadas', 'estado']

class LocalidadSerializer(serializers.ModelSerializer):
    municipio = MunicipioSerializer(read_only=True)

    class Meta:
        model = Localidad
        fields = ['cve_loc', 'nomgeo', 'ambito', 'latitud', 'longitud', 'altitud', 'pob_total', 'total_viviendas_habitadas', 'municipio']

class AsentamientoSerializer(serializers.ModelSerializer):
    localidad = LocalidadSerializer(read_only=True)

    class Meta:
        model = Asentamiento
        fields = ['cve_asen', 'nom_asen', 'tipo_asen', 'localidad']