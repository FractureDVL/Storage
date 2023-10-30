from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(verbose_name=('Nombre'), max_length=100, unique=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self) -> str:
        return self.nombre