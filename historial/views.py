from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import historiaForm
from gestion.models import Historial

# Create your views here.

class HistoriaList(ListView):
    model=Historial
    template_name='historial/historia.html'

class HistoriaCreate(CreateView):
    model=Historial
    form_class=historiaForm
    template_name='historial/crearHisto.html'
    success_url=reverse_lazy('IndexHisto')

class HistoriaUpdate(UpdateView):
    model=Historial
    form_class=historiaForm
    template_name='historial/crearHisto.html'
    success_url=reverse_lazy('IndexHisto')

class HistoriaDelete(DeleteView):
    model=Historial
    template_name='historial/verificacion.html'
    success_url=reverse_lazy('IndexHisto')

