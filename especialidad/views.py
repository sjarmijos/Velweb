from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import especialidadForm
from gestion.models import Especialidad


# Create your views here.

class EspecialidadList(ListView):
    model=Especialidad
    template_name='especialidad/espe.html'

class EspecialidadCreate(CreateView):
    model= Especialidad
    form_class= especialidadForm
    template_name='especialidad/crearEspe.html'
    success_url=reverse_lazy('IndexEspe')

class EspecialidadActualizar(UpdateView):
    model= Especialidad
    form_class=especialidadForm
    template_name='especialidad/crearEspe.html'
    success_url=reverse_lazy('IndexEspe')

class EspecialidadEliminar(DeleteView):
    model=Especialidad
    template_name='especialidad/verificacion.html'
    success_url=reverse_lazy('IndexEspe')
