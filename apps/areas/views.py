# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy

from apps.areas.models import Area
from apps.areas.forms import AreaForm

from apps.personas.models import Persona

# Create your views here.
#Vistas del modelo area

class AreaCreate(CreateView):
    model = Area
    form_class = AreaForm
    template_name = 'areas/area_form.html'
    success_url = reverse_lazy('areas:listado_areas') #esta url se debe cambiar hacia el listado

class AreaList(ListView):
    model = Area
    template_name = 'areas/area_list.html'

def PersonaArea(request, ar_id):
    persona = Persona.objects.distinct().filter(areas=ar_id)
    template = 'areas/area_persona.html'
    context = {'personas':persona}
    return render(request, template, context)
