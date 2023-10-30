from django.contrib import admin
from apps.core.models.proveedor import Proveedor
from apps.core.models.proveedor import ProveedorProducto

# INLINE
class ProveedorProductoInline(admin.StackedInline):
    model = ProveedorProducto

# ADMIN
class ProveedorAdmin(admin.ModelAdmin):
    inlines = [ProveedorProductoInline] 

# REGISTER
admin.site.register(Proveedor, ProveedorAdmin)