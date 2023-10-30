from rest_framework.viewsets import ModelViewSet
from apps.core.models.historial import ProductoPedido
from apps.core.models.historial import Pedido
from apps.core.models.historial import Historial
from apps.core.serializers.producto_pedido import ProductoPedidoSerializer
from apps.core.serializers.producto_pedido import PedidoSerializer
from apps.core.serializers.producto_pedido import HistorialSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from datetime import date
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from apps.core.models.producto import Producto
from apps.core.serializers.producto import ProductoSerializer

#pedido, producto, precio, cantidad, talla
class ProductoPedidoViewSet(ModelViewSet):
    model = ProductoPedido
    serializer_class = ProductoPedidoSerializer
    queryset = ProductoPedido.objects.all()

    permission_classes = [IsAuthenticated]
    @action(detail=False, methods=['post'], url_path='agregar-producto')
    def agregarProductos(self, request):
        productos = self.request.data.get('productos')
        #productos = request.data.get('productos', [])

        if not productos:
            return Response({'mensaje': 'No se encuentran productos en el carrito'}, status=status.HTTP_400_BAD_REQUEST)

        user_id = self.request.user.id
        user = User.objects.get(pk=user_id)
        pedido = {"fecha": date.today(), "usuario": user.id,  "estado": True}
        pedido_serializer = PedidoSerializer(data=pedido)

        if pedido_serializer.is_valid():
            pedido = pedido_serializer.save()
        else:
            return Response(pedido_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            precioTotal = 0;
            for producto_data in productos:
                buscar_producto = Producto.objects.get(pk=producto_data.get('producto'))

                producto_data['pedido'] = pedido.id
                producto_data['precio'] = buscar_producto.precio
                serializer = ProductoPedidoSerializer(data=producto_data)
                precioTotal += buscar_producto.precio * producto_data.get('cantidad')

                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            descuento = self.request.data.get('descuento')
            precioTotal -= precioTotal*descuento/100
            pedido.precio_total = precioTotal
            pedido.save()
        except buscar_producto.DoesNotExist:
            pedido.delete()
            return Response({'mensaje': 'Productos invalidos'}, status=status.HTTP_400_BAD_REQUEST)
        
            

        return Response({'datos':{
                    'mensaje':f'Realizando pedido',
                    'total_a_pagar': precioTotal
                }}, status=status.HTTP_200_OK)

class PedidoViewSet(ModelViewSet):
    model = Pedido
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()

class HistorialViewSet(ModelViewSet):
    model = Historial
    serializer_class = HistorialSerializer
    queryset = Historial.objects.all()



