from functools import update_wrapper
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .forms import citaForm
from gestion.models import Cita

# Create your views here.

class CitaList(ListView):
    model=Cita
    template_name='cita/cita.html'

class CitaCreate(CreateView):
    model=Cita
    form_class=citaForm
    template_name='cita/crearCita.html'
    success_url=reverse_lazy('IndexCita')

class CitaActualizar(UpdateView):
    model=Cita
    form_class=citaForm
    template_name='cita/crearCita.html'
    success_url=reverse_lazy('IndexCita')

class CitaEliminar(DeleteView):
    model=Cita
    template_name='cita/verificacion.html'
    success_url=reverse_lazy('IndexCita')
