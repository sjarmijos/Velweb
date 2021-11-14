from django import urls
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import MedicoList,MedicoCreate, MedicoActualizar, MedicoDelete

urlpatterns=[
    path('', login_required(MedicoList.as_view()), name='IndexMedico'),
    path('crearMedico/', login_required(MedicoCreate.as_view()), name='crearMed'),
    path('editarMedico/<str:pk>', login_required(MedicoActualizar.as_view()), name='editarMed'),
    path('elminarMedico/<str:pk>', login_required(MedicoDelete.as_view()), name='eliminarMed'),
]