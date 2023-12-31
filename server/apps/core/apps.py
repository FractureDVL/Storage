from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'

    def ready(self):
        import apps.core.admin.categoria
        import apps.core.admin.proveedor
        import apps.core.admin.producto
        import apps.core.admin.producto_pedido
        import apps.core.signals
