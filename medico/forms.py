from django import forms
from django.forms import fields
from gestion.models import Medico

class medicoForm(forms.ModelForm):
    class Meta:
        model=Medico
        fields='__all__'
        