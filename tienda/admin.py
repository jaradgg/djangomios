from django.contrib import admin
from . models import CategoriaProd, Producto


# Register your models here.

class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")
    
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")
    
# registramos las clases
admin.site.register(Producto, ProductoAdmin)
admin.site.register(CategoriaProd, CategoriaProdAdmin)