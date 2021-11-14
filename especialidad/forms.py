from django import forms
from django.forms import fields
from gestion.models import Especialidad

class especialidadForm(forms.ModelForm):
    class Meta:
        model=Especialidad
        fields='__all__'
