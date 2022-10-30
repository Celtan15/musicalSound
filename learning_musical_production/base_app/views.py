from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'base_app/login.html/')
    
def sign_up(request):
    return render(request, 'base_app/sign_up.html/')

def home(request):
    return render(request, 'base_app/home.html/')

'''
def learning_interface(request):
    return render(request, 'base_app/learning_interface.html/')
'''

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