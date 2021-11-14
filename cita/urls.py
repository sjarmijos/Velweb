from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import CitaList, CitaCreate, CitaActualizar, CitaEliminar

urlpatterns=[
    path('', login_required(CitaList.as_view()), name='IndexCita'),
    path('crearCita/', login_required(CitaCreate.as_view()), name='crearCita'),
    path('editarCita/<str:pk>', login_required(CitaActualizar.as_view()), name='editarCita'),
    path('eliminarCita/<str:pk>', login_required(CitaEliminar.as_view()), name='eliminarCita'),
]