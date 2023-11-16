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
from core.views import index, contato, dados_url
from core.views import  curso_cadastro, cursos, curso_editar, curso_remover
from core.views import cadastrar_area, area,editar_area, deletar_area,perfil,autenticar, desconectar, cadastrar

# metodos do django 
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/',autenticar, name= 'login'),   
    path('logout/',desconectar, name = 'logout'),
    path('cadastrar/',cadastrar, name = 'cadastrar'),



    path('perfil/', perfil, name='perfil'),
    path('admin/', admin.site.urls),
    path('', index, name= 'home'),
    path('contato/',contato,name='contato'),
    path('dados_url/<str:sobrenome>/<int:idade>/<str:nota>/',dados_url,name='dados_url'),

    path('cursos/',cursos,name='cursos'),
    path('curso_cadastro/',curso_cadastro,name='curso_cadastro'),
    path('curso_editar/<int:id>/', curso_editar, name='curso_editar'),
    path('curso_remover/<int:id>/', curso_remover, name='curso_remover'),

    path('cadastrar_area/', cadastrar_area,name='cadastrar_area'),
    path('area/',area,name='area'),
    path('editar_area/<int:id>/',editar_area,name='editar_area'),
    path('deletar_area/<int:id>',deletar_area,name='deletar_area'),


]
