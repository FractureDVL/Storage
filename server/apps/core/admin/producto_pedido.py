from django.contrib import admin
from apps.core.models.historial import ProductoPedido

#Inline
class ProductoPedidoInline(admin.StackedInline):
    model = ProductoPedido

#Admin

#Register
admin.site.register(ProductoPedido)
