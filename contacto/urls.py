# para cada aplicación creamos su url path que luego usaremos en el urls del proyecto
# importamos el path desde django
from django.urls import path

#importamos las vistas del proyecto proyecto contacto
from . import views

urlpatterns = [
    
    path('', views.contacto, name="Contacto"),

]
