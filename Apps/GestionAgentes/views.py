from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from ASR.Apps.GestionAgentes.models import Agente


def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)

def inicio(request):
    agente = Agente.objects.all()  #Obtenemos los datos de la base
    datos = {'agentes':agente}   #Almacenamos y nombramos para usar en el HTML
    return render(request, 'index.html', datos)

def estado(request, host, comunidad): #Recibimos datos del agente
    dato1 = {'host': host, 'comunidad': comunidad}  #Los almacenamos y nombramos para usarlos en el HTML
    #dato3 = {'v': vSNMP}
    return render(request, 'estadoAg.html', dato1)
