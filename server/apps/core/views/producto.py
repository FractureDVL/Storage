from django.forms import ValidationError
from rest_framework.viewsets import ModelViewSet
from apps.core.models.categoria import Categoria
from apps.core.models.producto import Producto
from apps.core.serializers.producto import ProductoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

#✅
class ProductoViewSet(ModelViewSet):
    model= Producto
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()
    http_method_names = ['get']
        
        
        