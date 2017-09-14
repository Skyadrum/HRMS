# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Area(models.Model):
    nombre_area = models.CharField(max_length = 30)
    clave_area = models.CharField(max_length = 12)
    descripcion = models.TextField()

    def __unicode__(self):
        return self.nombre_area
