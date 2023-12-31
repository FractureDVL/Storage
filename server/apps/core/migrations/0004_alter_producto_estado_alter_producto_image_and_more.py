# Generated by Django 4.0.5 on 2023-10-28 20:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_historial_options_alter_producto_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Activo 🥲'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='El precio no puede ser negativo')], verbose_name='Precio'),
        ),
        migrations.AlterUniqueTogether(
            name='coleccion_producto',
            unique_together={('producto', 'coleccion')},
        ),
    ]
