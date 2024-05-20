# para cada aplicación creamos su url path que luego usaremos en el urls del proyecto
# importamos el path desde django
from django.urls import path

#importamos las vistas de la app autenticacion
from .views import VRegistro, cerrar_sesion, loguear


urlpatterns = [
    
    path('', VRegistro.as_view(), name="Autenticacion"),
    path('cerrar_sesion/', cerrar_sesion, name="cerrar_sesion"),
    path('loguear/', loguear, name="loguear"),

]
