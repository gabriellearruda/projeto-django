"""impulsoprevine URL Configuration

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
from django.urls import path
from django.conf.urls import url, include
from django.http import HttpResponse
from .view import Inicio, DadosAdm, Graficos, Impulso, Indicadores, Previne
from django.conf.urls.static import static
from django.conf import settings


def home(request):
    return HttpResponse('Welcome to the Tinyapp\'s Homepage!')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dados/', DadosAdm.as_view(), name='dados'),
    path('grafico/', Graficos.as_view(), name='graficos'),
    path('', Inicio.as_view(), name='inicio'),
    path('impulso/', Impulso.as_view(), name='impulso'),
    path('previne/', Previne.as_view(), name='previne'),
    path('indicadores/', Indicadores.as_view(), name='indicadores')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)