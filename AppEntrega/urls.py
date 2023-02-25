from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio, name = 'pagina principal'),
    path('NoValid', construccion, name = 'under_construction'),
    path('proveedores', proveedores, name = 'proveedores'),
    path('productos', productos, name = "productos"),
    path('vendedores', vendedores, name= "vendedores"),
    path('resultados-proveedores', respuesta_proveedores, name='resultados-proveedores'),
    path('resultados-vendedores', respuesta_vendedores, name="resultados-vendedores"),
    path('resultados-productos', respuesta_productos, name="resultados-productos")
]