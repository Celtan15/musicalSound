from django.shortcuts import render
from django.http import HttpResponse
from interface_module_app.forms import Feedback_form
from base_app.models import Options_panel, Side_panel, Workstation, Top_panel
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

#Esto aún no es funcional para el proyecto, pero es la manera correcta para capturar respuestas y pasarlas a otra url,
#más adelante servirá para poder recoger las respuestas de los usuarios en la evaluacion del modulo
'''
def interface_answer(request):
    return render(request, 'answers.html')

def test(request):
    if request.GET['int_ev']:
        mensaje='Respuesta dada: %r' %request.GET['int_ev']
    else:
        mensaje='No has seleccionado una respuesta'
    return HttpResponse(mensaje)
'''

def learning_interface(request):
    return render(request, 'learning_mixture.html')

def learning_options_panel(request):
    options_panel=Options_panel.objects.all()
    return render(request, 'learning_concepts.html', {'options_panel': options_panel})

def learning_side_panel(request):
    side_panel=Side_panel.objects.all()
    return render(request, 'learning_basic_techniques.html', {'side_panel': side_panel})
   
def learning_top_panel(request):
    top_panel=Top_panel.objects.all()
    return render(request, 'learning_mixture.html', {'top_panel': top_panel})

def learning_workstation(request):
    workstation=Workstation.objects.all()
    return render(request, 'learning_glossary.html', {'workstation': workstation})