from django.urls import path
from Contenido.views import *

urlpatterns=[
    path('', Incio , name='Incio'),
    path('mision/', mision, name='mision'),
    path('desplegable/', desplegable, name='desplegable'),##Extra
    path('formulario/', formulario, name='formulario'),
    path('APIrets/', APIrets, name='APIrets'), ##Extra
    path('index/', index ,name='index'),
    path('crear/', crear, name='crear'),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name="modificar"),
    path('login/', login, name="login"), ##No se logra implementar, sin embargo, si se puede hacer que inicie sesión como admin
    path('base',base,name="base"), ##Se le encuentra relevancia muy tarde 

    path('tienda',tienda,name="tienda"),
    path('agregar_producto/<id>', agregar_producto, name="agregar_producto"),
    path('eliminar_producto/<id>', eliminar_producto, name="eliminar_producto"),
    path('restar_producto/<id>', restar_producto, name="restar_producto"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
    path('generarBoleta/', generarBoleta,name="generarBoleta"),
]