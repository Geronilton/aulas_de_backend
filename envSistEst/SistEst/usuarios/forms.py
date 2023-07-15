from django import forms
from django.contrib.auth.models import User

class RegisterForms(forms.ModelForm):
    class Meta:
        model = User
        fields =[ 'first_name', 'last_name', 'username', 'email', 'password']
        labels = {'first_name' : 'Digite seu primeeiro nome',
                    'last_name' : 'Digite seu ultimo nome',
                    'username' : 'Digite seu username',
                    'email' : 'Digite o seu email',
                    'password' : 'Digite sua senha '
                    }
        help_texts = {
            'email' : 'O email deve ter um /@',
            'password' : 'cria uma senha forte com caracteres, numeros e simbolos especias',
        }
        error_mensages = {
            'username' : {
                'required' : 'Este campo não pode ser vazio'
            }
        }

        widgets = {
            'first_name' : forms.TextInput(attrs ={ 
                'placeholder' : 'Primeiro Nome',
                'required' : 'true'
        }),
            'password' : forms.PasswordInput(attrs ={
                'placeholder' : 'senha',
            })
        }