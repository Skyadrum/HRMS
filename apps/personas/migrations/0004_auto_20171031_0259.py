# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-31 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0003_auto_20171031_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='motivo_baja',
            field=models.CharField(blank=True, choices=[('Despido', 'Despido'), ('Renuncia', 'Renuncia'), ('Otro', 'Otro')], max_length=40, null=True),
        ),
    ]
