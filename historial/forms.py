from django import forms
from gestion.models import Historial

class historiaForm(forms.ModelForm):
    class Meta:
        model=Historial
        fields='__all__'