# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-31 01:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='fecha_baja',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='motivo_baja',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='observaciones',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
