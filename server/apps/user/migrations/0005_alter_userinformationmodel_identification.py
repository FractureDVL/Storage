# Generated by Django 4.0.5 on 2023-10-29 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_userinformationmodel_identification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformationmodel',
            name='identification',
            field=models.CharField(max_length=15, unique=True, verbose_name='Documento de identidad'),
        ),
    ]
