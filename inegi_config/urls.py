"""
URL configuration for inegi_config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# Vista básica para la raíz del sitio
def home(request):
    return HttpResponse("¡Hola, mundo! Esta es la página de inicio.")

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home),  # ← Añade esta línea
    path('', include('inegi_app.urls')),
    # Ruta para el esquema OpenAPI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    
    # UI de Swagger
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
