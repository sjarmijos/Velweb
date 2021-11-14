from django.urls import path
from django.urls.exceptions import NoReverseMatch
from django.contrib.auth.decorators import login_required
from .views import Pacientelist, PacienteCreate, PacienteUpdate, PacienteDelete

urlpatterns=[
    path('',login_required(Pacientelist.as_view()), name="IndexPac"),
    path('crearPaciente/',login_required(PacienteCreate.as_view()), name="crearPac"),
    path('editarPaciente/<int:pk>', login_required(PacienteUpdate.as_view()), name="editarPac"),
    path('elminarPaciente/<int:pk>', login_required(PacienteDelete.as_view()), name="eliminarPac"),
]