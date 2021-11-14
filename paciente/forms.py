from django import forms
from django.forms import fields
from gestion.models import Paciente

class pacienteForm(forms.ModelForm):
    class Meta:
        model=Paciente
        fields='__all__'
        