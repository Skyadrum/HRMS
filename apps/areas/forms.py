# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django import forms
from apps.areas.models import Area

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area

        fields = [
            'nombre_area',
            'clave_area',
            'descripcion',
        ]

        labels = {
            'nombre_area':'Nombre del Area',
            'clave_area':'Clave del Area',
            'descripcion':'Descripcion',
        }

        widgets = {
            'nombre_area':forms.TextInput(attrs={'class':'form-control'}),
            'clave_area':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
        }
