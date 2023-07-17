from django.urls import path, include
from usuarios.views import *

app_name = 'usuarios'

urlpatterns = [
    path("register/", register_view, name = 'register'),
    path("register/<int:firstacess>", register_view, name = 'register'),
    path("register/create", register_create, name = 'create'),
    path("login/", login_view, name = 'login'),
    path("login/acess", login_acess, name = 'acess'),
    #path("login/logout", register_create, name = 'logout'),
    path("area_usuario", area_usuario_view, name = 'area_usuario'),
]