from rest_framework import viewsets
from .models import Estado, Municipio, Localidad, Asentamiento
from .serializers import EstadoSerializer, MunicipioSerializer, LocalidadSerializer, AsentamientoSerializer
from .pagination import LocalidadPagination, AsentamientoPagination
# from .filters import AsentamientoFilter
from drf_spectacular.utils import extend_schema, OpenApiParameter

# Parámetros reutilizables
PARAM_ESTADO = OpenApiParameter(name='estado', type=str, description='Clave del estado (2 dígitos)', required=False)
PARAM_MUNICIPIO = OpenApiParameter(name='municipio', type=str, description='Clave del municipio (3 dígitos)', required=False)
PARAM_LOCALIDAD = OpenApiParameter(name='localidad', type=str, description='Clave de la localidad (4 dígitos)', required=False)
PARAM_ASENTAMIENTO = OpenApiParameter(name='asentamiento', type=str, description='Clave del asentamiento (4 dígitos)', required=False)

@extend_schema(
    description="Lista estados o filtra por cve_ent",
    parameters=[PARAM_ESTADO],
)
class EstadoViewSet(viewsets.ModelViewSet):
    serializer_class = EstadoSerializer
    lookup_field = 'cve_ent'

    def get_queryset(self):
        estado_cve = self.request.query_params.get('estado')
        
        queryset = Estado.objects.all()

        if estado_cve:
            queryset = queryset.filter(cve_ent=estado_cve)

        return queryset

@extend_schema(
    description="Lista municipios o filtra por estado o municipio",
    parameters=[PARAM_ESTADO, PARAM_MUNICIPIO],
)
class MunicipioViewSet(viewsets.ModelViewSet):
    serializer_class = MunicipioSerializer
    lookup_field = 'cve_mun'

    def get_queryset(self):
        estado_cve = self.request.query_params.get('estado')
        municipio_cve = self.request.query_params.get('municipio')

        queryset = Municipio.objects.select_related('estado')

        if estado_cve:
            queryset = queryset.filter(estado__cve_ent=estado_cve)
        if municipio_cve:
            queryset = queryset.filter(cve_mun=municipio_cve)

        return queryset

@extend_schema(
    description="Lista localidades o filtra por estado, municipio o localidad",
    parameters=[PARAM_ESTADO, PARAM_MUNICIPIO, PARAM_LOCALIDAD],
)
class LocalidadViewSet(viewsets.ModelViewSet):
    pagination_class = LocalidadPagination
    serializer_class = LocalidadSerializer
    lookup_field = 'cve_loc'

    def get_queryset(self):
        estado_cve = self.request.query_params.get('estado')
        municipio_cve = self.request.query_params.get('municipio')
        localidad_cve = self.request.query_params.get('localidad')

        queryset = Localidad.objects.select_related('municipio__estado')

        if estado_cve:
            queryset = queryset.filter(municipio__estado__cve_ent=estado_cve)
        if municipio_cve:
            queryset = queryset.filter(municipio__cve_mun=municipio_cve)
        if localidad_cve:
            queryset = queryset.filter(cve_loc=localidad_cve)

        return queryset

@extend_schema(
    description="Lista asentamientos o filtra por estado, municipio, localidad o asentamiento",
    parameters=[PARAM_ESTADO, PARAM_MUNICIPIO, PARAM_LOCALIDAD, PARAM_ASENTAMIENTO],
)
class AsentamientoViewSet(viewsets.ModelViewSet):
    pagination_class = AsentamientoPagination
    serializer_class = AsentamientoSerializer
    lookup_field = 'cve_asen'

    def get_queryset(self):
        estado_cve = self.request.query_params.get('estado')
        municipio_cve = self.request.query_params.get('municipio')
        localidad_cve = self.request.query_params.get('localidad')
        asentamiento_cve = self.request.query_params.get('asentamiento')

        queryset = Asentamiento.objects.select_related('localidad__municipio__estado')

        if estado_cve:
            queryset = queryset.filter(localidad__municipio__estado__cve_ent=estado_cve)
        if municipio_cve:
            queryset = queryset.filter(localidad__municipio__cve_mun=municipio_cve)
        if localidad_cve:
            queryset = queryset.filter(localidad__cve_loc=localidad_cve)
        if asentamiento_cve:
            queryset = queryset.filter(cve_asen=asentamiento_cve)

        return queryset