# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.conf.urls import url, include

from apps.areas.views import AreaCreate, AreaList, PersonaArea
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^nueva_area/', AreaCreate.as_view(), name='nueva_area'),
    url(r'^listado_areas/', AreaList.as_view(), name='listado_areas'),
    url(r'^persona_areas/(?P<ar_id>\d+)/$', PersonaArea, name='persona_areas'),
]
