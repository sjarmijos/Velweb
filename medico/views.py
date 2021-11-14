from typing import ContextManager
from django.http.request import HttpRequest
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from gestion.models import Medico
from .forms import medicoForm

# Create your views here.

class MedicoList(ListView):
    model=Medico
    template_name='medico/med.html'

class MedicoCreate(CreateView):
    model=Medico
    form_class=medicoForm
    template_name='medico/crearMedico.html'
    success_url=reverse_lazy('IndexMedico')

class MedicoActualizar(UpdateView):
    model=Medico
    form_class=medicoForm
    template_name='medico/crearMedico.html'
    success_url=reverse_lazy('IndexMedico')

class MedicoDelete(DeleteView):
    model=Medico
    template_name='medico/verificacion.html'
    success_url=reverse_lazy('IndexMedico')
