from django import forms
from django.forms import fields, widgets
from gestion.models import Cita

class citaForm(forms.ModelForm):
    class Meta:
        model=Cita
        fields='__all__'
        widgets={
            'fecha_cita': forms.DateInput(attrs={'type':'date'}),
            'hora_cita': forms.TimeInput(attrs={'type':'time'}),
        }