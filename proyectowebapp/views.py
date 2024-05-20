from django.shortcuts import render

from carro.carro import Carro

# Create your views here.
def home(request):
    
    # inicializamos el carro aquí para tenerlo disponible en todo el proyecto
    carro = Carro(request)
    
    return render(request, 'proyectowebapp/home.html')