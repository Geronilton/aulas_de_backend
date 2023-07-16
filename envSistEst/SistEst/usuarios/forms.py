from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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

    def clean_email(self):
        data = self.cleaned_data.get("email")

        if not '@' in data:
            raise ValidationError(
                'O campo e-mail deve apresentar um @',
                code='invalid'
            )
        
        return data
    
    def clean(self):
        cleaned_data = super().clean()

        pass1 = cleaned_data.get("password")
        pass2 = cleaned_data.get("password2")

        if pass1 != pass2:
            raise ValidationError(
                {"password" : "Ambos passwords devem ser iguais"}
            )


    email = forms.CharField(
        required = True,
        max_length = 150,
        help_text=(
            'Digite um email valido'
        )
    )

    password2 = forms.CharField(required=True,
            label= 'Repita seu password',
            widget = forms.PasswordInput(attrs ={
                'placeholder' : 'senha',  
            })                     
        )