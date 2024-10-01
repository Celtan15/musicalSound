from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.contrib.auth.models import User
from .models import Pregunta, ElegirRespuesta, RespuestaUsuario

'''
class Login_form(forms.Form):
    email=forms.EmailField(label='Email', required=True)
    password=forms.CharField(label='Pdw', required=True)
'''

class Sign_up_form(UserCreationForm):
    name = forms.CharField(
            label='Nombre',
            max_length=50,
            widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(
        label='Nickname',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    country = CountryField(blank_label='(Seleccionar país)').formfield(
        widget=CountrySelectWidget(attrs={'class': 'form-control'})
    )
    date_birth = forms.DateField(
        label='Fecha de nacimiento',
        required=True,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    phone = forms.CharField(
        label='Número de teléfono',
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'country', 'date_birth', 'phone', 'password1', 'password2']
        help_texts = {k: '' for k in fields}

class ElegirInlineFormset(forms.BaseInlineFormSet):
    def clean(self):
        super(ElegirInlineFormset, self).clean()
        res_correcta = 0
        for formulario in self.forms:
            if not formulario.is_valid():
                return

            if formulario.cleaned_data and formulario.cleaned_data.get('correcta_elegir') is True:
                res_correcta += 1

        try:
            assert res_correcta == Pregunta.NUM_RES_PERMITIDAS
        except AssertionError:
            raise forms.ValidationError('Ingrese solo una respuesta')
