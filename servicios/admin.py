from django.contrib import admin
from . models import Servicio

# para que aparezcan los campos de solo lectura
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# Register your models here.
admin.site.register(Servicio, ServicioAdmin)