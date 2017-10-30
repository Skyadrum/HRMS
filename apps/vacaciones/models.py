# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import models
import datetime

from apps.personas.models import Persona
# Create your models here.

class Vacaciones(models.Model):
    dias_tomados = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    razon = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=50)
    id_solicitante = models.CharField(max_length=13, default=0)
    personas = models.ForeignKey(Persona, null=True, blank=True)

    def __get__dias(self):
        today = datetime.date.today()
        ingreso = self.personas.fecha_ingreso

        return (today.year - ingreso.year)*10

    dias_vacaciones = property(__get__dias)

    def __get__restantes(self):
        today = datetime.date.today()
        ingreso = self.personas.fecha_ingreso
        total = (today.year - ingreso.year)*10
        restante = total - int(self.dias_tomados)

        return restante


    dias_restantes = property(__get__restantes)


class Permisos(models.Model):
    opciones = [('Económico', 'Económico'), ('Especial', 'Especial')]

    dias_tomados = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    tipo = models.CharField(max_length=50, choices=opciones)
    observaciones = models.CharField(max_length=50)
    id_solicitante = models.CharField(max_length=13, default=0)
    personas = models.ForeignKey(Persona, null=True, blank=True)
