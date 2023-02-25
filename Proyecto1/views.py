from django.template import loader
from django.shortcuts import render

def inicio(request):
    return render(request,'AppEntrega/inicio.html')
