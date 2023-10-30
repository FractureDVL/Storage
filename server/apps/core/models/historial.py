from django.contrib.auth.models import User
from apps.core.models.producto import Producto
from django.db import models
#Pedidos 
class Pedido(models.Model):
    fecha = models.DateTimeField(auto_now=True,editable=False, verbose_name='Fecha', null=False)
    usuario = models.ForeignKey(User, verbose_name='Usuario', null=False, on_delete=models.DO_NOTHING)
    estado = models.BooleanField(default=False, verbose_name='Estado de producto', null=False)
    precio_total = models.DecimalField(verbose_name='Precio total', null=True, decimal_places=5, max_digits=25)
    
    class Meta: 
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
    
    def __str__(self) -> str:
        return f'{self.pk}, {self.fecha }, {self.usuario.pk}, {self.estado}, {self.precio_total}'

#Historia de pedidos de un usuario
class Historial(models.Model): 
    pedido = models.ForeignKey(Pedido, verbose_name='Pedido', null=False, on_delete=models.DO_NOTHING)
    class Meta: 
        verbose_name = 'Historial'
        verbose_name_plural = 'Historial'

#Productos / pedidos
class ProductoPedido(models.Model):
    pedido = models.ForeignKey(Pedido, verbose_name='Pedido',on_delete=models.CASCADE, null=True, blank=True)
    producto = models.ForeignKey(Producto,verbose_name='Producto', null=False, on_delete=models.DO_NOTHING, default='')
    precio = models.DecimalField(verbose_name='Precio', null=False, decimal_places=5, max_digits=25)
    cantidad = models.IntegerField(verbose_name='Cantidad', null=False)
    talla = models.IntegerField(verbose_name='Talla')

    class Meta: 
        verbose_name = 'Producto pedido'

    def __str__(self) -> str:
        return f'{self.producto }, {self.pedido}'