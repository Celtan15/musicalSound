from cmath import log
from email import message
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

def login_request(request):
    if(request.method=='POST'):
        form=AuthenticationForm(request, data=request.POST)
        if(form.is_valid):
            user=form.cleaned_data.get('nickname')
            pdw=form.cleaned_data.get('password')

    form=AuthenticationForm()
    return render(request, 'registration/login.html/', {'form': form})

def logout_request(request):
    logout(request)
    message.info(request, 'Tu sesión ha sido cerrada con éxito')
    return redirect('')

def sign_up(request):
    form=UserCreationForm
    return render(request, 'base_app/sign_up.html/', {'form':form})

def home(request):
    return render(request, 'base_app/home.html/')

'''
def learning_interface(request):
    return render(request, 'base_app/learning_interface.html/')
'''

@login_required
def learning_mixture(request):
    return render(request, 'base_app/learning_mixture.html/')
    
@login_required
def learning_mastering(request):
    return render(request, 'base_app/learning_mastering.html/')

@login_required    
def tips(request):
    return render(request, 'base_app/tips.html/')
    
@login_required
def evaluations(request):
    return render(request, 'base_app/evaluations.html/')

def who_we_are(request):
    return render(request, 'base_app/who_we_are.html/')

def about(request):
    return render(request, 'base_app/about.html/')

def feedback(request):
    return render(request, 'base_app/feedback.html/')

@login_required
def index(request):
    return render(request, 'base_app/index.html/')