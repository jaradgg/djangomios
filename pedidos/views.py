from django.contrib import messages
from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from carro.carro import Carro

from pedidos.models import LineaPedido, Pedido

from django.core.mail import send_mail

from django.template.loader import render_to_string

from django.utils.html import strip_tags

from .models import Producto

# Create your views here.

@login_required(login_url = "/autenticacion/loguear")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user = request.user)
    carro = Carro(request)
    lineas_pedidos = list()
    
    for key, value in carro.carro.items():
        lineas_pedidos.append(LineaPedido(
            producto = Producto.objects.get(id=key),
            cantidad = value["cantidad"], # para acceder al valor del diccionario
            user = request.user,
            pedido = pedido
        ))


    LineaPedido.objects.bulk_create(lineas_pedidos)
    
    enviar_mail( 
        pedido = pedido, 
        lineas_pedidos = lineas_pedidos, 
        nombreusuario = request.user.username, 
        emailusuario = request.user.email
    )
    
    messages.success(request, "El pedido se ha creado correctamente")
    
    return redirect('../tienda')  
 

def enviar_mail(**kwargs):
    asunto = "Gracias por el pedido"
    mensaje = render_to_string("emails/pedido.html",{
        "pedido":kwargs.get("pedido"),
        "lineas_pedidos":kwargs.get("lineas_pedidos"),
        "nombreusuario":kwargs.get("nombreusuario")
    })
    
    mensaje_texto = strip_tags(mensaje)
    from_email = "correoeodk@gmail.com"
    to_mail = str(kwargs.get("emailusuario"))
    
    send_mail( 
        asunto, 
        mensaje_texto,
        from_email, 
        [to_mail], 
        html_message=mensaje,
        fail_silently=False        
    )