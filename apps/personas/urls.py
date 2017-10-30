# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.conf.urls import url, include
from apps.personas.views import PersonaCreate, PersonaList, PersonaUpdate, PersonaDelete, PersonaInfo,\
PersonaInicio, PersonaFormato

from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^inicio_persona$', PersonaInicio, name='inicio_persona'),
    url(r'^nueva_persona$', PersonaCreate.as_view(), name='nueva_persona'),
    url(r'^listado_persona$', PersonaList.as_view(), name='listado_persona'),
    url(r'^info_persona/(?P<pk>\d+)$', PersonaInfo, name='info_persona'),
    url(r'^persona_formato/(?P<pk>\d+)$', PersonaFormato, name='persona_formato'),
    # url(r'^vacaciones_hist/(?P<pk>\d+)$', PersonaVacacionesHist, name='vacaciones_hist'),
    # url(r'^persona_vacaciones/(?P<pk>\d+)$', login_required(PersonaVacaciones), name='persona_vacaciones'),
    url(r'^editar_persona/(?P<pk>\d+)$', PersonaUpdate.as_view(), name='editar_persona'),
    url(r'^eliminar_persona/(?P<pk>\d+)$', PersonaDelete.as_view(), name='eliminar_persona'),
]
