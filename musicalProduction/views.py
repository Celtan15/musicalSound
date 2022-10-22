from django.http import HttpResponse

def test(request):
    return HttpResponse('Intento # mil')

def despedida(request):
    return HttpResponse('Adiós')