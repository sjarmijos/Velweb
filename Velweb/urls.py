"""Velweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from gestion.views import indexIni


urlpatterns = [
    path('',indexIni, name="home"),
    path('admin/', admin.site.urls),
    path('gestion/', include('gestion.urls')),
    path('paciente/', include('paciente.urls')),
    path('medico/', include('medico.urls')),
    path('especialidad/', include('especialidad.urls')),
    path('citas/', include('cita.urls')),
    path('historial/', include('historial.urls')),
    path('sesion/', include('loginout.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


