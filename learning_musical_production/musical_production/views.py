from django.http import HttpResponse
from django.shortcuts import render

#Simplemente sirve para probar que la página funcione correctamente
def test(request):
    return render(request,'template_test.html',{}) #Se pueden poner diccionarios con información, de momento no necesito nada

#Aquí pruebo las plantillas con cabecera y pie de página y los cambios dinámicos
def templates_testing(request):
    return render(request,'base_template.html',{})

