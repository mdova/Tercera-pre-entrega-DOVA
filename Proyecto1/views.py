from django.template import loader
from django.http import HttpResponse

def hola(request):
    diccionario = {}
    plantilla = loader.get_template('primer_template.html')
    contexto = plantilla.render(diccionario)
    return HttpResponse(contexto) 