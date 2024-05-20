# para cada aplicación creamos su url path que luego usaremos en el urls del proyecto
# importamos el path desde django
from django.urls import path

#importamos las vistas del proyecto proyecto proyectowebapp
from . import views

app_name = "carro"  # name space, para evitar coliciones de nombre de rutas en otras app

urlpatterns = [
    
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar'),
    path('restar/<int:producto_id>/', views.restar_producto, name='restar'),
    path('limpiar/', views.limpiar_carro, name='limpiar'),

]
