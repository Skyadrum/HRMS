# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import pdfkit
from django.template.loader import render_to_string

from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

from apps.vacaciones.forms import VacacionesForm, PermisosForm
from apps.vacaciones.models import Vacaciones, Permisos

from apps.personas.models import Persona

# Create your views here.
#Vacaciones
def AsignaVacaciones(request, pk):
    persona = Persona.objects.get(id=pk)
    if request.method == 'POST':
        form = VacacionesForm(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.persona = persona
            instance.save()
        return redirect('personas:listado_persona')
    else:
        form = VacacionesForm()
    return render(request, 'vacaciones/vacaciones_form.html', {'vacaciones':form, 'personas':persona})

def VacacionesPersona(request, pk):
    personas = Persona.objects.get(id=pk)
    context = {'vacaciones':personas}
    return render(request, 'personas/persona_info.html', context)


def PersonaVacacionesHist(request, pk):
    vacaciones = Vacaciones.objects.all().filter(id_solicitante=pk)
    personas = Persona.objects.all().filter(id=pk)
    rendered = render_to_string('formatos/vacaciones_hist.html', {'personas':personas, 'vacaciones':vacaciones})
    # Create a URL of our project and go to the template route
    pdf = pdfkit.from_string(rendered, False)
    # Generate download
    response = HttpResponse(pdf, content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="ourcodeworld.pdf"'

    return response

#Permisos
def AsignaPermisos(request, pk):
    persona = Persona.objects.get(id=pk)
    if request.method == 'POST':
        form = PermisosForm(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.persona = persona
            instance.save()
        return redirect('personas:listado_persona')
    else:
        form = PermisosForm()
    return render(request, 'permisos/permisos_form.html', {'permisos':form, 'personas':persona})

def PersonaPermisosHist(request, pk):
    permisos = Permisos.objects.all().filter(id_solicitante=pk)
    personas = Persona.objects.all().filter(id=pk)
    rendered = render_to_string('formatos/permisos_hist.html', {'personas':personas, 'permisos':permisos})
    # Create a URL of our project and go to the template route
    pdf = pdfkit.from_string(rendered, False)
    # Generate download
    response = HttpResponse(pdf, content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="ourcodeworld.pdf"'

    return response
