from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from .forms import pacienteForm
from gestion.models import Paciente


# Create your views here.s

class Pacientelist(ListView):
    model=Paciente
    template_name='paciente/paci.html'

class PacienteCreate(CreateView):
    model=Paciente
    form_class=pacienteForm
    template_name='paciente/crearPaciente.html'
    success_url=reverse_lazy('IndexPac')

class PacienteUpdate(UpdateView):
    model=Paciente
    form_class=pacienteForm
    template_name='paciente/crearPaciente.html'
    success_url=reverse_lazy('IndexPac')

class PacienteDelete(DeleteView):
    model=Paciente
    template_name="paciente/verificacion.html"
    success_url=reverse_lazy('IndexPac')