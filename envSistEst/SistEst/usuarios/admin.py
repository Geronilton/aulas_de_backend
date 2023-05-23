from django.contrib import admin
from usuarios.models import Usuarios, Carros,Estacionamentos
# Register your models here.


class UsuarioAdmin(admin.ModelAdmin):
    ...

class CarrosAdmin(admin.ModelAdmin):
    ...

class EstacionamentosAdmin(admin.ModelAdmin):
    ...
admin.site.register(Usuarios,UsuarioAdmin)

admin.site.register(Carros,CarrosAdmin)

admin.site.register(Estacionamentos, EstacionamentosAdmin)