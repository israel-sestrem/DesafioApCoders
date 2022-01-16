"""apcoders URL Configuration

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
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from .views import inicio, unidade_nao_existe, form_erro_validacao

urlpatterns = [
    path('admin/', admin.site.urls),
    path('despesas/', include('despesas.urls')),
    path('inquilinos/', include('inquilinos.urls')),
    path('unidades/', include('unidades.urls')),
    path('unidade_nao_existe', unidade_nao_existe, name='unidadeNaoExiste'),
    path('form_erro_validacao', form_erro_validacao, name='formErroValidacao'),
    path('', inicio, name='inicio')
]
