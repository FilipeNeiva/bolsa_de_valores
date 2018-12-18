"""bolsa_de_valores URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from bolsa.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('empresas', lista_empresas, name = 'empresas'),
    path('acoes', lista_acoes, name = 'acoes'),
    path('cotacoes', lista_cotacoes, name = 'cotacoes'),
    path('add_empresa', add_empresa, name = 'add_empresa'),
    path('add_acao', add_acao, name = 'add_acao'),
    path('add_cotacao', add_cotacao, name = 'add_cotacao')
]
