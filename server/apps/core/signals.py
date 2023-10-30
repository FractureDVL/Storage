from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from apps.core.models.categoria import Categoria
from apps.core.models.producto import Producto
@receiver(post_migrate)
def create_product_default(sender, **kwargs):
    productos = [
        {'nombre': 'Zapatos Nike', 'descripcion': 'Descripción de los zapatos Nike', 'precio': 50, 'categoria_nombre': 'Calzado', 'estado': True, 'image': 'ruta/a/la/imagen1.jpg'},
        {'nombre': 'Camiseta Adidas', 'descripcion': 'Descripción de la camiseta Adidas', 'precio': 30, 'categoria_nombre': 'Ropa Deportiva', 'estado': True, 'image': 'ruta/a/la/imagen2.jpg'},
        {'nombre': 'Portátil HP', 'descripcion': 'Descripción del portátil HP', 'precio': 800, 'categoria_nombre': 'Electrónicos', 'estado': True, 'image': 'ruta/a/la/imagen3.jpg'},
        {'nombre': 'Libro "El Principito"', 'descripcion': 'Descripción del libro "El Principito"', 'precio': 15, 'categoria_nombre': 'Libros', 'estado': True, 'image': 'ruta/a/la/imagen4.jpg'},
        {'nombre': 'Reloj Casio', 'descripcion': 'Descripción del reloj Casio', 'precio': 50, 'categoria_nombre': 'Accesorios', 'estado': True, 'image': 'ruta/a/la/imagen5.jpg'},
        {'nombre': 'Bicicleta Mountain Bike', 'descripcion': 'Descripción de la bicicleta Mountain Bike', 'precio': 300, 'categoria_nombre': 'Deportes', 'estado': True, 'image': 'ruta/a/la/imagen6.jpg'},
        {'nombre': 'Mochila Escolar', 'descripcion': 'Descripción de la mochila escolar', 'precio': 25, 'categoria_nombre': 'Accesorios Escolares', 'estado': True, 'image': 'ruta/a/la/imagen7.jpg'},
        {'nombre': 'Cámara Canon EOS', 'descripcion': 'Descripción de la cámara Canon EOS', 'precio': 600, 'categoria_nombre': 'Fotografía', 'estado': True, 'image': 'ruta/a/la/imagen8.jpg'},
        {'nombre': 'Silla de Oficina', 'descripcion': 'Descripción de la silla de oficina', 'precio': 80, 'categoria_nombre': 'Muebles', 'estado': True, 'image': 'ruta/a/la/imagen9.jpg'},
        {'nombre': 'Juego de Té Porcelana', 'descripcion': 'Descripción del juego de té de porcelana', 'precio': 40, 'categoria_nombre': 'Hogar', 'estado': True, 'image': 'ruta/a/la/imagen10.jpg'}
    ]
    Producto.objects.all().delete()
    for producto in productos:
        categoria, created = Categoria.objects.get_or_create(nombre=producto['categoria_nombre'])
        Producto.objects.create(
            nombre=producto['nombre'],
            descripcion=producto['descripcion'],
            precio=producto['precio'],
            categoria=categoria,
            estado=producto['estado'],
            image=producto['image']
        )
    print('se crearon los productos')
