from django import forms
from .models import curso, Area, Publico, Usuario
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'cpf', 'email', 'nome_completo', 'data_nascimento', 'password1', 'password2']


class CursosForm(forms.ModelForm):
    class Meta:
        model = curso
        fields = ['titulo', 'data_inicio', 'vagas','area','publico']
        widgets = {
            'area' : forms.RadioSelect(),
            'publico': forms.CheckboxSelectMultiple(),
        }


class AreasForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nome']



class PublicoForm(forms.ModelForm):
    class Meta:
        model = Publico
        fields = ['nome']