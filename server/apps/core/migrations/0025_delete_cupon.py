# Generated by Django 4.0.5 on 2023-10-30 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_remove_proveedor_fecha_remove_proveedor_hora_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cupon',
        ),
    ]