# Generated by Django 4.2.6 on 2024-04-25 10:37

import Aplicacion.menu.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plato',
            name='fecha_caducidad',
            field=models.DateTimeField(default=Aplicacion.menu.models.default_fecha_caducidad),
        ),
        migrations.AddField(
            model_name='plato',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
