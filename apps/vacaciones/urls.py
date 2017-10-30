# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.conf.urls import url, include
from apps.vacaciones.views import AsignaVacaciones, VacacionesPersona, AsignaPermisos, PersonaVacacionesHist,\
PersonaPermisosHist

from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^asignar_vacaciones/(?P<pk>\d+)$', AsignaVacaciones, name='asignar_vacaciones'),
    url(r'^info_persona/(?P<pk>\d+)$', VacacionesPersona, name='info_persona'),
    url(r'^vacaciones_hist/(?P<pk>\d+)$', PersonaVacacionesHist, name='vacaciones_hist'),
    url(r'^permisos_hist/(?P<pk>\d+)$', PersonaPermisosHist, name='permisos_hist'),

    #Permisos
    url(r'^asignar_permisos/(?P<pk>\d+)$', AsignaPermisos, name='asignar_permisos'),
]
