from django.urls import path
from . import views



urlpatterns = [
    path('crear/cliente/', views.registrar_cliente, name='crear_factura_cliente'),
    path('crear/productos/', views.registrar_productos, name='crear_factura_productos'),
    path('crear/insumos/', views.registrar_insumos, name='crear_factura_insumos'),
    path('crear/coste/', views.registrar_coste_servicio, name='crear_factura_coste'),
    path('crear/adelanto/', views.registrar_adelanto, name='crear_factura_adelanto'),
    path('crear/observaciones/', views.registrar_observaciones, name='crear_factura_observaciones'),
    path('crear/finalizar/', views.finalizar_factura, name='finalizar_factura'),
    path('<int:factura_id>/', views.detalle_factura, name='detalle_factura'),
    path('buscar/cliente/', views.buscar_cliente, name='buscar_cliente'),
    path('buscar/producto/', views.buscar_producto, name='buscar_producto'),
    path('buscar/insumo/', views.buscar_insumo, name='buscar_insumo'),
]
