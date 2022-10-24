from django.shortcuts import render
from django.http import HttpResponse
from interface_module_app.forms import Feedback_form

#Esto aún no es funcional para el proyecto, pero es la manera correcta para capturar respuestas y pasarlas a otra url,
#más adelante servirá para poder recoger las respuestas de los usuarios en la evaluacion del modulo
def interface_answer(request):
    return render(request, 'answers.html')

def test(request):
    if request.GET['int_ev']:
        mensaje='Respuesta dada: %r' %request.GET['int_ev']
    else:
        mensaje='No has seleccionado una respuesta'
    return HttpResponse(mensaje)

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
