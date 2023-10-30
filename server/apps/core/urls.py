from django.urls import path, include
from rest_framework import routers
from apps.core.views.producto import ProductoViewSet
from apps.core.views.producto_pedido import ProductoPedidoViewSet

app_name = 'core'
router = routers.DefaultRouter()
##Configurar rutas 
router.register(prefix='product', viewset=ProductoViewSet, basename='product')
router.register(prefix='pedido', viewset=ProductoPedidoViewSet, basename='pedido')
#
#

urlpatterns = [
    path('auth/', include('apps.authentication.urls')),
    path('user/', include('apps.user.urls')),
    path('', include(router.urls))   
]
