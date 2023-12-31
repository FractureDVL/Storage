# Generated by Django 4.0.5 on 2023-10-28 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_coleccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColeccionProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coleccion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.coleccion', verbose_name='Coleccion')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.producto', verbose_name='Producto')),
            ],
            options={
                'verbose_name': 'Coleccion/Producto',
                'verbose_name_plural': 'Colecciones/Productos',
                'unique_together': {('producto', 'coleccion')},
            },
        ),
    ]
