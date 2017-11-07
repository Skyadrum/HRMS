# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.conf.urls import url, include
from apps.personas.views import PersonaCreate, PersonaList, PersonaUpdate, PersonaDelete, PersonaInfo,\
PersonaInicio, PersonaFormato, PersonaListInactive, PersonaInactivePdf, PersonaFormatoBaja

from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^inicio_persona$', login_required(PersonaInicio), name='inicio_persona'),
    url(r'^nueva_persona$', login_required(PersonaCreate.as_view()), name='nueva_persona'),
    url(r'^listado_persona$', login_required(PersonaList.as_view()), name='listado_persona'), #activos
    url(r'^baja_persona$', login_required(PersonaListInactive.as_view()), name='baja_persona'), #inactivos
    url(r'^baja_list$', login_required(PersonaInactivePdf), name='baja_list'), #inactivosPDF
    url(r'^info_persona/(?P<pk>\d+)$', login_required(PersonaInfo), name='info_persona'),
    url(r'^persona_formato/(?P<pk>\d+)$', login_required(PersonaFormato), name='persona_formato'),
    url(r'^persona_formato_baja/(?P<pk>\d+)$', login_required(PersonaFormatoBaja), name='persona_formato_baja'), #PDF
    # url(r'^vacaciones_hist/(?P<pk>\d+)$', PersonaVacacionesHist, name='vacaciones_hist'),
    # url(r'^persona_vacaciones/(?P<pk>\d+)$', login_required(PersonaVacaciones), name='persona_vacaciones'),
    url(r'^editar_persona/(?P<pk>\d+)$', login_required(PersonaUpdate.as_view()), name='editar_persona'),
    url(r'^eliminar_persona/(?P<pk>\d+)$', login_required(PersonaDelete.as_view()), name='eliminar_persona'),
]
