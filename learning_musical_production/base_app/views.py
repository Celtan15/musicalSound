from cmath import log
from email import message
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate, login
from base_app.models import Login
from base_app.forms import Sign_up_form
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Inicia sesión al usuario
                messages.success(request, f"Bienvenido {username}")
                return redirect('Index')  # Redirige a la página principal
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    else:
        form = AuthenticationForm()

    return render(request, 'base_app/login.html', {'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, 'Tu sesión ha sido cerrada con éxito')
    return redirect('')

def sign_up(request):
    if request.method == 'POST':
        form = Sign_up_form(request.POST)
        if form.is_valid():
            user = form.save()  # Guarda el usuario y almacénalo en la variable 'user'
            nickname = form.cleaned_data.get('username')
            messages.success(request, f'Usuario: {nickname} fue creado con éxito')

            # Autentica al usuario recién creado
            user = authenticate(request, username=nickname, password=form.cleaned_data.get('password1'))

            if user is not None:
                login(request, user)  # Inicia sesión al usuario
                return redirect('Index')  # Redirige a la página principal o donde prefieras
    else:
        form = Sign_up_form()

    return render(request, 'base_app/sign_up.html', {'form': form})

def home(request):
    return render(request, 'base_app/home.html/')

def learning_mixture(request):
    return render(request, 'base_app/learning_mixture.html/')
    
def learning_mastering(request):
    return render(request, 'base_app/learning_mastering.html/')
    
def tips(request):
    return render(request, 'base_app/tips.html/')
    
def evaluations(request):
    return render(request, 'base_app/evaluations.html/')

def who_we_are(request):
    return render(request, 'base_app/who_we_are.html/')

def about(request):
    return render(request, 'base_app/about.html/')

def feedback(request):
    return render(request, 'base_app/feedback.html/')

def index(request):
    return render(request, 'base_app/index.html/')
    
''' A continuación el método para enviar emails con form, email de usuario hace referencia al email loggeado en la
aplicacion, mientras que send mail aún no se ha construido, revisar el documento TO DO para ver más informacion
def feedback(request):
    if request.method=='POST':
        form=Feedback_form(request.POST)
        if form.is_valid():
            infForm=form.cleaned_data

            send_mail(infForm['issue'], infForm['msg'], emailDelUsuario, ['correoCreadoParaLaAplicacion'])

            return render(request, 'formularioDeAgradecimiento.html')
    else:
        form=Feedback_form()
    return render(request, 'feedback_form.html', {'form': form})
'''
