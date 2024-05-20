# para cada aplicación creamos su url path que luego usaremos en el urls del proyecto
# importamos el path desde django
from django.urls import path

#importamos las vistas del proyecto proyecto proyectowebapp
from . import views

# con <int:categoria_id> convertimos string a int
urlpatterns = [
    
    path('', views.blog, name="Blog"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
    
]

