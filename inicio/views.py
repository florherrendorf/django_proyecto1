from datetime import datetime

from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render

from inicio.models import Auto
import random


def inicio(request):
    contexto = {}
    return render(request, 'inicio/home.html', contexto)

def bienvenida(request):
    contexto = {}
    return render(request, 'inicio/bienvenida.html', contexto)

def fecha_y_hora(request):
    fecha_hora = datetime.now()  
    return HttpResponse(f'''<h1>Esta vista muestra la hora actual.</h1>
{fecha_hora}''') 
    
    
def saludo(request, nombre, apellido):
    respuesta = f'Buenas, como va {nombre.title()} {apellido.title()}?'
    return HttpResponse(respuesta) 


def mi_template(request):
        
    archivo_abierto = open('inicio/mi_template.html')
    template = Template(archivo_abierto.read())
    archivo_abierto.close()
    
    contexto = Context({"nombre": "Pepe"})   # es la info que queremos pasarle al template
    template_renderizado = template.render(contexto)    # ES PARA QUE ENTIENDA EL HTML
    
    # with open('templates\mi_template.html') as archivo_abierto:
        # template = Template(archivo_abierto.read())
    
    respuesta = template_renderizado
    
    return HttpResponse(respuesta) 


def mi_template2(request):
          
    template = loader.get_template('inicio/mi_template2.html')
    
    diccionario = {"nombre": "Pepe"}   # es la info que queremos pasarle al template
    template_renderizado = template.render(diccionario)    # ES PARA QUE ENTIENDA EL HTML
    
    respuesta = template_renderizado
    
    return HttpResponse(respuesta) 


def mi_template3(request):

    return render(request, 'inicio/mi_template3.html', {"nombre": "Pepe"}) 


def condicionales_y_bucles(request):
    
    diccionario = {
        "nombre": "Ricardo",
        "mis_elementos": [22],
        "numeros": list(range(15))
    }
    
    return render(request, 'inicio/condicionales_y_bucles.html', diccionario)


def crear_auto(request, marca, modelo, anio):
    auto = Auto(marca=marca, modelo=modelo, anio=anio)
    auto.save()
    
    contexto = {'auto': auto }
    return render(request, 'inicio/crear_auto.html', contexto)