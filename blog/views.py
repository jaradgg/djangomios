from django.shortcuts import render
from . models import Post, Categoria

# Create your views here.

def blog(request):
    
    posts= Post.objects.all()

    
    return render(request, 'blog/blog.html', {"posts": posts})

# vista para poder elegir las categorias en la plantilla
def categoria(request, categoria_id):
    
    categoria = Categoria.objects.get(id=categoria_id)
    
    # filtramos por categoria
    posts = Post.objects.filter(categorias=categoria)
    return render(request, 'blog/categoria.html', {'categoria': categoria, 'posts': posts})