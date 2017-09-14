# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django import forms

from apps.personas.models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona

        fields = [
            'imagen',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'fecha_nacimiento',
            'curp',
            'rfc',
            'sexo',
            'calle',
            'numero_interior',
            'numero_exterior',
            'colonia',
            'codigo_postal',
            'pais',
            'estado',
            'municipio',
            'telefono',
            'celular',
            'correo',
            'datos_adicionales',
            'areas',
            'cargo',
            'fecha_ingreso',
            'id_persona',
        ]

        labels = {
            'imagen':'Imagen',
            'nombre':'Nombre',
            'apellido_paterno':'Apellido paterno',
            'apellido_materno':'Apellido materno',
            'fecha_nacimiento':'Fecha de nacimiento',
            'curp':'CURP',
            'rfc':'RFC',
            'sexo':'Sexo',
            'calle':'Calle',
            'numero_interior':'Número interior',
            'numero_exterior':'Número exterior',
            'colonia':'Colonia',
            'codigo_postal':'Codigo postal',
            'pais':'País',
            'estado':'Estado',
            'municipio':'Municipio',
            'telefono':'Teléfono',
            'celular':'Celular',
            'correo':'Correo',
            'datos_adicionales':'Datos adicionales',
            'areas':'Area',
            'cargo':'Cargo',
            'fecha_ingreso':'Fecha de Ingreso',
            'id_persona':'Id Empleado',
        }

        widgets = {
            'imagen': forms.FileInput,
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class':'form-control'}),
            'curp': forms.TextInput(attrs={'class':'form-control'}),
            'rfc': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.Select(attrs={'class':'form-control'}),
            'calle': forms.TextInput(attrs={'class':'form-control'}),
            'numero_interior': forms.TextInput(attrs={'class':'form-control'}),
            'numero_exterior': forms.TextInput(attrs={'class':'form-control'}),
            'colonia': forms.TextInput(attrs={'class':'form-control'}),
            'codigo_postal': forms.TextInput(attrs={'class':'form-control'}),
            'pais': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={'class':'form-control'}),
            'municipio': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'celular': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.TextInput(attrs={'class':'form-control'}),
            'datos_adicionales': forms.Textarea(attrs={'class':'form-control'}),
            'areas': forms.Select(attrs={'class':'form-control'}),
            'cargo':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_ingreso':forms.TextInput(attrs={'class':'form-control'}),
            'id_persona': forms.TextInput(attrs={'class':'form-control'}),
        }
