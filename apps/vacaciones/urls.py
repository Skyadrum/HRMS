# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.conf.urls import url, include
from apps.vacaciones.views import AsignaVacaciones, VacacionesPersona, AsignaPermisos

from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^asignar_vacaciones/(?P<pk>\d+)$', AsignaVacaciones, name='asignar_vacaciones'),
    url(r'^info_persona/(?P<pk>\d+)$', VacacionesPersona, name='info_persona'),

    #Permisos
    url(r'^asignar_permisos/(?P<pk>\d+)$', AsignaPermisos, name='asignar_permisos'),
]
