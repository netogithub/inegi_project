from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import EstadoViewSet, MunicipioViewSet, LocalidadViewSet, AsentamientoViewSet

default_router = DefaultRouter()
default_router.register(r'estados', EstadoViewSet, basename='estado')
default_router.register(r'municipios', MunicipioViewSet, basename='municipio')
default_router.register(r'localidades', LocalidadViewSet, basename='localidad')
default_router.register(r'asentamientos', AsentamientoViewSet, basename='asentamiento')

# urlpatterns = [
#     path('', include(router.urls)),
# ]

simple_router = routers.SimpleRouter()
simple_router.register(r'estados', EstadoViewSet, basename='estado')

municipios_router = routers.NestedSimpleRouter(simple_router, r'estados', lookup='estado')
municipios_router.register(r'municipios', MunicipioViewSet, basename='municipio')

localidades_router = routers.NestedSimpleRouter(municipios_router, r'municipios', lookup='municipio')
localidades_router.register(r'localidades', LocalidadViewSet, basename='localidad')

asentamientos_router = routers.NestedSimpleRouter(localidades_router, r'localidades', lookup='localidad')
asentamientos_router.register(r'asentamientos', AsentamientoViewSet, basename='asentamiento')

urlpatterns = [
    path('', include(default_router.urls)),
    # path('api/', include(simple_router.urls)),
    # path('api/', include(municipios_router.urls)),
    # path('api/', include(localidades_router.urls)),
    # path('api/', include(asentamientos_router.urls)),
]
