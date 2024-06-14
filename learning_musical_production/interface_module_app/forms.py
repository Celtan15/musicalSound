from django import forms
from django.forms import CharField

#Este formulario ayudará para recibir correos electrónicos más adelante
class Feedback_form(forms.Form):
    issue=forms.CharField
    msg=forms.CharField