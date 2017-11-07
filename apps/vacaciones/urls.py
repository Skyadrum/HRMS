# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.conf.urls import url, include
from apps.vacaciones.views import AsignaVacaciones, VacacionesPersona, AsignaPermisos, PersonaVacacionesHist,\
PersonaPermisosHist, VacacionesList, PermisosList, VacacionesHist, PermisosHist

from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^asignar_vacaciones/(?P<pk>\d+)$', login_required(AsignaVacaciones), name='asignar_vacaciones'),
    url(r'^info_persona/(?P<pk>\d+)$', login_required(VacacionesPersona), name='info_persona'),
    url(r'^vacaciones_hist/(?P<pk>\d+)$', login_required(PersonaVacacionesHist), name='vacaciones_hist'),
    url(r'^vacaciones_list$', login_required(VacacionesList.as_view()), name='vacaciones_list'),
    url(r'^vacaciones_historial$', login_required(VacacionesHist), name='vacaciones_historial'),

    #Permisos
    url(r'^asignar_permisos/(?P<pk>\d+)$', login_required(AsignaPermisos), name='asignar_permisos'),
    url(r'^permisos_hist/(?P<pk>\d+)$', login_required(PersonaPermisosHist), name='permisos_hist'),
    url(r'^permisos_list$', login_required(PermisosList.as_view()), name='permisos_list'),
    url(r'^permisos_historial$', login_required(PermisosHist), name='permisos_historial'),
]
