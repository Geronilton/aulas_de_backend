from django.contrib import admin
from usuarios.models import Usuarios
# Register your models here.


class UsuarioAdmin(admin.ModelAdmin):
    ...
    
admin.site.register(Usuarios,UsuarioAdmin)