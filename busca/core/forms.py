from django import forms
from .models import Curso, Area, Usuario, Publico
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'cpf', 'email', 
        'nome_completo', 'data_nascimento',
        'password1', 'password2']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'vagas', 'data_inicio', 'area', 'publico']
        widgets = {
            'area' : forms.RadioSelect(),
            'publico': forms.CheckboxSelectMultiple(),
        }

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nome']

class PublicoForm(forms.ModelForm):
    class Meta:
        model = Publico
        fields = ['nome']