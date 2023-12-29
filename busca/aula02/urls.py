"""
URL configuration for aula02 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from core.views import home, contato, dados_url
from core.views import cursos, curso_cadastro, curso_editar, curso_remover
from core.views import areas, area_cadastro, publicos, publico_cadastro
from core.views import perfil, autenticar, desconectar, cadastrar

urlpatterns = [
    path('login/', autenticar, name='login'),
    path('logout/', desconectar, name='logout'),
    path('cadastrar/', cadastrar, name='cadastrar'),

    path('perfil/', perfil, name='perfil'),

    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contato/', contato, name='contato'),
    path('dados_url/<str:sobrenome>/<int:idade>/<str:nota>/', dados_url, name='dados_url'),

    path('cursos/', cursos, name='cursos'),
    path('curso_cadastro/', curso_cadastro, name='curso_cadastro'),
    path('curso_editar/<int:id>/', curso_editar, name='curso_editar'),
    path('curso_remover/<int:id>/', curso_remover, name='curso_remover'),

    path('areas/', areas, name='areas'),
    path('area_cadastro/', area_cadastro, name='area_cadastro'),

    path('publicos/', publicos, name='publicos'),
    path('publico_cadastro/', publico_cadastro, name='publico_cadastro'),
]