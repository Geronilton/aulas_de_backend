from django.urls import path, include
from usuarios.views import *

app_name = 'usuarios'

urlpatterns = [
    path("register/", register_view, name = 'register'),
     path("register/create", register_create, name = 'create'),
]