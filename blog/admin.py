from django.contrib import admin
from . models import Categoria, Post

# Register your models here.

# para agregar al panel de admin
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# registro en el panel de admin
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
