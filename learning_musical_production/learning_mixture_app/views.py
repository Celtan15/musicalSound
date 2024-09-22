from django.shortcuts import render
from django.http import HttpResponse
from interface_module_app.forms import Feedback_form
from base_app.models import Concepts, Basic_techniques, Mid_techniques, Glossary

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

def learning_mixture(request):
    return render(request, 'learning_mixture.html')

def learning_concepts(request):
    concepts=Concepts.objects.all()
    return render(request, 'learning_concepts.html', {'learning_concepts': concepts})

def learning_basic_techniques(request):
    basic=Basic_techniques.objects.all()
    return render(request, 'learning_basic_techniques.html', {'learning_basic_techniques': basic})
   
def learning_mid_techniques(request):
    mid=Mid_techniques.objects.all()
    return render(request, 'learning_mid_techniques.html', {'learning_mid_techniques': mid})

def learning_glossary(request):
    glossary=Glossary.objects.all()
    return render(request, 'learning_glossary.html', {'workstation': glossary})