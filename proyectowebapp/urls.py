# para cada aplicación creamos su url path que luego usaremos en el urls del proyecto
# importamos el path desde django
from django.urls import path

#importamos las vistas del proyecto proyecto proyectowebapp
from proyectowebapp import views

# configuramos las urls de las imagenes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.home, name="Home"), 
    
]

# agregamos al urlpatterns la ubicación de las imágenes para mostrarlas
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

