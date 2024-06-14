from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

'''
class Login_form(forms.Form):
    email=forms.EmailField(label='Email', required=True)
    password=forms.CharField(label='Pdw', required=True)
'''

class Sign_up_form(UserCreationForm):
    name=forms.CharField(label='Nombre',max_length=50)
    password1=forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
    username=forms.CharField(label='Nickname', max_length=50)
    email=forms.EmailField(label='Email', required=True)
    country=forms.CharField(label='País de residencia', max_length=30)
    date_birth=forms.DateField(label='Fecha de nacimiento')
    phone=forms.CharField(label='Número de teléfono', max_length=20)

    class Meta():
        model=User
        fields=['name', 'password1', 'password2', 'username', 'email', 'country', 'date_birth', 'phone']
        help_texts={k:'' for k in fields}

