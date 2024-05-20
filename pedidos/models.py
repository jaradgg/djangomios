from django.db import models
from django.contrib.auth import get_user_model
from tienda.models import Producto
from django.db.models import F, Sum, FloatField

# Create your models here.
User = get_user_model() # para tener al usuario logueado


class Pedido(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "pedidos"
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ["id"]
    id: int  # anotación del tipo del atributo id para que se identifique el atributo id de la tabla.

    def __str__(self):
        return str(self.id)

    @property
    def total(self):
        return self.lineas.aggregate(
            total=Sum(F("producto__precio") * F("cantidad"), output_field=FloatField)
        )["total"] or 0.0

        
# tabla linea de pedidos
class LineaPedido(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, related_name="lineas", on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cantidad} unidades de {self.producto.nombre}"

    class Meta:
        db_table = "lineapedidos"
        verbose_name = "Linea Pedido"
        verbose_name_plural = "Lineas Pedidos"
        ordering = ["id"]
