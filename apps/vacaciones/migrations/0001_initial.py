# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-14 21:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dias_tomados', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateField()),
                ('razon', models.CharField(max_length=50)),
                ('observaciones', models.CharField(max_length=50)),
                ('id_solicitante', models.CharField(default=0, max_length=13)),
                ('personas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personas.Persona')),
            ],
        ),
    ]