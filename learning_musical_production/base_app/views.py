from cmath import log
from email import message
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate, login
from base_app.models import Login
from .models import Evaluations, RespuestaUsuario
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

    EvaluacionUser, created = Evaluations.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        pregunta_pk = request.POST.get('pregunta_pk')
        preg_respondida = EvaluacionUser.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
        respuesta_pk = request.POST.get('respuesta_pk')

        try:
            opcion_seleccionada = preg_respondida.pregunta.opciones.get(pk = respuesta_pk)
        except ObjectDoesNotExist:
            raise Http404

        EvaluacionUser.validar_intento(preg_respondida, opcion_seleccionada)

        return redirect ('Evaluations_answers', preg_respondida.pk)

    else:
        pregunta = EvaluacionUser.nuevas_preguntas()
        if pregunta is not None:
            EvaluacionUser.nuevos_intentos(pregunta)

        context = {
            'pregunta':pregunta
        }
    return render(request, 'base_app/evaluations_questions.html/', context)

def resultado_pregunta(request, preg_respondida_pk):
    respondida = get_object_or_404(RespuestaUsuario, pk=preg_respondida_pk)

    context = {
        'respondida':respondida
    }
    return render(request, 'base_app/evaluations_answers.html', context)

def who_we_are(request):
    return render(request, 'base_app/who_we_are.html/')

def module_evaluations(request):
    return render(request, 'base_app/evaluations.html/')

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
