"""
URL configuration for proyectoweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path


 # no nesecito importar las vistas ya que las voy a usar en cada urls de cada app.
""" 
import proyectowebapp.views
import servicios.views
import tienda.views
import blog.views
import contactos.views 
"""
 # las url de las app las saco del url del proyecto y las llevo a cada app
""" 
    path('', proyectowebapp.views.home, name="Home"),
    path('servicios/', servicios.views.servicios, name="Servicios"),
    path('tienda/', tienda.views.tienda, name="Tenda"),
    path('blog/', blog.views.blog, name="Blog"),
    path('contacto/', contactos.views.contacto, name="Contacto"), 
"""
# cada aplicación debe iniciar con '' el path y luego la funcion include
# para enlazar las app del proyecto usamos la funcion include
   

urlpatterns = [ 
    
    path("admin/", admin.site.urls),
    
    
    
    path('blog/', include('blog.urls')),
    
    path('contacto/', include('contacto.urls')),
    
    path('autenticacion/', include('autenticacion.urls')),
    
    path('servicios/', include('servicios.urls')),
    
    path('tienda/', include('tienda.urls')),
    
    path('carro/', include('carro.urls')),
    
    path('pedidos/', include('pedidos.urls')),
        
    path('', include('proyectowebapp.urls')),
    
]


