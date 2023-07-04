from django.urls import path, include
from usuarios.views import *

urlpatterns = [
    path("register/", register_view, name = 'register'),
]