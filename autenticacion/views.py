from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect


# Create your views here.

""" def autenticacion(request):
    
    return render(request, 'registro/registro.html') """
    
class VRegistro(View):
    
    def get(self, request):
        
        form = UserCreationForm()
        
        return render(request, 'registro/registro.html', {'form': form})
    
    def post(self, request):
        
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            usuario = form.save()
            
            login(request, usuario)
            
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
                
            return render(request, 'registro/registro.html', {'form': form})
    
def cerrar_sesion(request):
   logout(request)
   
   return redirect('Home') 

# vista para logeo de usuarios
@csrf_protect
def loguear(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            contrasegna = form.cleaned_data.get('password')
            usuario = authenticate(username=nombre_usuario, password=contrasegna)
            
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                messages.error(request, 'Username or password incorrect')
        
        else:    
            messages.error(request, 'Incorrect information')
        
    form = AuthenticationForm()
    
    return render(request, 'login/login.html', {'form': form})
    