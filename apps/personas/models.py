# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import models
from apps.areas.models import Area

import datetime

# Create your models here.

class Persona(models.Model):
    opciones = [('masculino', 'Masculino'), ('femenino', 'Femenino')]

    imagen = models.ImageField(upload_to='usr/', blank=True, null=True)
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    curp = models.CharField(max_length=18)
    rfc = models.CharField(max_length=18)
    sexo = models.CharField(max_length=70, choices=opciones)
    #datos de domicilio
    calle = models.CharField(max_length=40)
    numero_interior = models.IntegerField(blank=True, null=True)
    numero_exterior = models.IntegerField(blank=True, null=True)
    colonia = models.CharField(max_length=40)
    codigo_postal = models.IntegerField()
    pais = models.CharField(max_length=40)
    estado = models.CharField(max_length=40)
    municipio = models.CharField(max_length=40)
    #datos de contacto
    telefono = models.CharField(max_length=13)
    celular = models.CharField(max_length=13)
    correo = models.EmailField()
    #adicionales
    datos_adicionales = models.TextField(blank=True, null=True)
    id_persona = models.CharField(max_length=13)
    fecha_ingreso = models.DateField()
    activo = models.IntegerField(default=1, editable=False)
    #llaves foraneas
    areas = models.ForeignKey(Area, blank=True, null=True)
    cargo = models.CharField(max_length=75)

    def __unicode__(self):
        return self.id_persona

    def __get__dias(self):
        today = datetime.date.today()
        ingreso = self.fecha_ingreso

        return (today.year - ingreso.year)*10

    vacaciones = property(__get__dias)
