from django.shortcuts import render
from servicios.models import Servicio  # ruta del modelo servicio

# Create your views here.
def servicios(request):
    
    # variable para recolectar los objetos dentro de la clase servicio
    servicios = Servicio.objects.all()
    
    # regreso los objetos a la vista para mostrarlos en la plantilla
    return render(request, 'servicios/servicios.html', {'servicios': servicios})