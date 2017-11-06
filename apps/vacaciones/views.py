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
from apps.areas.models import Area

# Create your views here.
#Vacaciones

class VacacionesList(ListView):
    model = Vacaciones
    template_name = 'vacaciones/vacaciones_list.html'

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

def VacacionesHist(request):
    vacaciones = Vacaciones.objects.all()
    personas = Persona.objects.all()
    rendered = render_to_string('formatos/vacaciones_solicitadas.html', {'personas':personas, 'vacaciones':vacaciones})
    # Create a URL of our project and go to the template route
    pdf = pdfkit.from_string(rendered, False)
    # Generate download
    response = HttpResponse(pdf, content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="ourcodeworld.pdf"'

    return response

#Permisos

class PermisosList(ListView):
    model = Permisos
    template_name = 'vacaciones/permisos_list.html'

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

def PermisosHist(request):
    permisos = Permisos.objects.all()
    personas = Persona.objects.all()
    rendered = render_to_string('formatos/permisos_solicitados.html', {'personas':personas, 'permisos':permisos})
    # Create a URL of our project and go to the template route
    pdf = pdfkit.from_string(rendered, False)
    # Generate download
    response = HttpResponse(pdf, content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="ourcodeworld.pdf"'

    return response
