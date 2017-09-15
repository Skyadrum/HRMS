# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

from apps.personas.models import Persona
from apps.personas.forms import PersonaForm

from apps.vacaciones.models import Vacaciones, Permisos

# Create your views here.
#Clases

class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'personas/persona_form.html'
    success_url = reverse_lazy('personas:listado_persona')


class PersonaList(ListView):
    model = Persona
    template_name = 'personas/persona_list.html'


class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'personas/persona_edit.html'
    success_url = reverse_lazy('personas:listado_persona')

    def get_context_data(self, **kwargs):
        context = super(PersonaUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        persona = self.model.objects.get(id=pk)
        if 'form' not in context:
            context['form'] = self.form_class()
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_personas = kwargs['pk']
        personas = self.model.objects.get(id=id_personas)
        form = self.form_class(request.POST, instance=personas)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class PersonaDelete(DeleteView):
    model = Persona
    template_name = 'personas/persona_delete.html'
    success_url = reverse_lazy('personas:listado_persona')

#Funciones
def PersonaInicio(request):
    context = {}
    return render(request, 'personas/persona_inicio.html', context)

def PersonaInfo(request, pk):
    personas = Persona.objects.get(id=pk)
    vacaciones = Vacaciones.objects.all().filter(id_solicitante=pk)
    permisos = Permisos.objects.all().filter(id_solicitante=pk)
    context = {'personas':personas, 'vacaciones':vacaciones, 'permisos':permisos}
    return render(request, 'personas/persona_info.html', context)


# def PersonaVacaciones(request, pk):
#     vacaciones = Vacaciones.objects.distinct().filter(id_solicitante=pk)
#     template = 'personas/persona_detail.html'
#     context = {'vacaciones':vacaciones }
#     return render(request, template, context)
