from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import HistoriaList, HistoriaCreate, HistoriaUpdate, HistoriaDelete

urlpatterns=[
    path('',login_required(HistoriaList.as_view()), name="IndexHisto"),
    path('crearHistoria/',login_required(HistoriaCreate.as_view()), name="crearHisto"),
    path('editarHistoria/<str:pk>', login_required(HistoriaUpdate.as_view()), name="editarHisto"),
    path('eliminarHistoria/<str:pk>', login_required(HistoriaDelete.as_view()), name="eliminarHisto"),
]