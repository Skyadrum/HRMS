# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django import forms

from apps.vacaciones.models import Vacaciones, Permisos

class VacacionesForm(forms.ModelForm):
    class Meta:
        model = Vacaciones

        fields = [
            'dias_tomados',
            'fecha_inicio',
            'razon',
            'observaciones',
            'id_solicitante',
        ]

        labels = {
            'dias_tomados': 'Días tomados',
            'fecha_inicio': 'Fecha de inicio',
            'razon': 'Razón',
            'observaciones': 'Observaciones',
            'id_solicitante': 'Clave del solicitante'
        }

        widgets = {
            'dias_tomados': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_inicio': forms.TextInput(attrs={'class':'form-control'}),
            'razon': forms.TextInput(attrs={'class':'form-control'}),
            'observaciones': forms.TextInput(attrs={'class':'form-control'}),
            'id_solicitante': forms.TextInput(attrs={'class':'form-control'}),
        }

class PermisosForm(forms.ModelForm):
    class Meta:
        model = Permisos

        fields = [
            'dias_tomados',
            'fecha_inicio',
            'tipo',
            'observaciones',
            'id_solicitante',
        ]

        labels = {
            'dias_tomados':'Días tomados',
            'fecha_inicio':'Fecha de inicio',
            'tipo':'Tipo',
            'observaciones':'Observaciones',
            'id_solicitante':'Id Solicitante',
        }

        widgets = {
            'dias_tomados': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_inicio': forms.TextInput(attrs={'class':'form-control'}),
            'tipos': forms.Select(attrs={'class':'form-control'}),
            'observaciones': forms.TextInput(attrs={'class':'form-control'}),
            'id_solicitante': forms.TextInput(attrs={'class':'form-control'}),
        }
