from rest_framework.pagination import PageNumberPagination

class EstadoPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'  # Permite cambiar el tamaño de página
    max_page_size = 200

class MunicipioPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 100

class LocalidadPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50

class AsentamientoPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50