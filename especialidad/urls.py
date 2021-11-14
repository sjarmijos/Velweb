from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import EspecialidadList, EspecialidadActualizar, EspecialidadCreate, EspecialidadEliminar

urlpatterns=[
    path('', EspecialidadList.as_view(), name='IndexEspe'),
    path('crearEspe/', login_required(EspecialidadCreate.as_view()), name='crearEspec'),
    path('editarEspe/<str:pk>',login_required(EspecialidadActualizar.as_view()), name='editarEspec'),
    path('eliminarEspe/<str:pk>',login_required(EspecialidadEliminar.as_view()), name='eliminarEspec'),
]