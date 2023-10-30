from datetime import date
from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MinValueValidator
from django.utils import timezone

# Registro de proveedor
class Proveedor(models.Model):
    proveedor = models.CharField(verbose_name=('Proveedor'), max_length=255, unique=True)
    class Meta: 
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
    
    def __str__(self) -> str:
        return self.proveedor
    
# relacion producto
class ProveedorProducto(models.Model):
    proveedor = models.ForeignKey("core.Proveedor", verbose_name=_("Proveedor"), on_delete=models.CASCADE) 
    producto = models.ForeignKey("core.Producto", verbose_name=_('Producto'), on_delete=models.CASCADE)
    cantidad = models.IntegerField(verbose_name=_('Cantidad'), validators=[MinValueValidator(0, message='El precio no puede ser negativo')])
    
    class Meta: 
        verbose_name_plural = 'Productos'
    
    def __str__(self) -> str:
        return f'{self.proveedor}'
    
# Historial de inventario 
class HistorialProveedor(models.Model):
    proveedor_producto = models.ForeignKey('core.ProveedorProducto', verbose_name='Proveedor', on_delete=models.CASCADE)
    hora = models.DateTimeField(verbose_name='Hora', default=timezone.now)
    fecha = models.DateField(verbose_name='Fecha', default=date.today)

