# Generated by Django 4.0.5 on 2023-10-30 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_productopedido_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='precio_Total',
            field=models.DecimalField(decimal_places=5, max_digits=25, null=True, verbose_name='Precio Total'),
        ),
    ]
