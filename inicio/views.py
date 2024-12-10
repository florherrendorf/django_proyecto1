from datetime import datetime

from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render

from inicio.models import Auto
import random


def bienvenida(request):
    respuesta = '<h1>Bienvenida!!!</h1>'
    return HttpResponse(respuesta) 

def fecha_y_hora(request):
    fecha_hora = datetime.now()  
    return HttpResponse(f'''<h1>Esta vista muestra la hora actual.</h1>
{fecha_hora}''') 
    
    
def saludo(request, nombre, apellido):
    respuesta = f'Buenas, como va {nombre.title()} {apellido.title()}?'
    return HttpResponse(respuesta) 


def mi_template(request):
        
    archivo_abierto = open('mi_template.html')
    template = Template(archivo_abierto.read())
    archivo_abierto.close()
    
    contexto = Context({"nombre": "Pepe"})   # es la info que queremos pasarle al template
    template_renderizado = template.render(contexto)    # ES PARA QUE ENTIENDA EL HTML
    
    # with open('templates\mi_template.html') as archivo_abierto:
        # template = Template(archivo_abierto.read())
    
    respuesta = template_renderizado
    
    return HttpResponse(respuesta) 


def mi_template2(request):
          
    template = loader.get_template('mi_template2.html')
    
    diccionario = {"nombre": "Pepe"}   # es la info que queremos pasarle al template
    template_renderizado = template.render(diccionario)    # ES PARA QUE ENTIENDA EL HTML
    
    respuesta = template_renderizado
    
    return HttpResponse(respuesta) 


def mi_template3(request):

    return render(request, 'mi_template3.html', {"nombre": "Pepe"}) 


def condicionales_y_bucles(request):
    
    diccionario = {
        "nombre": "Ricardo",
        "mis_elementos": [22],
        "numeros": list(range(15))
    }
    
    return render(request, 'condicionales_y_bucles.html', diccionario)


def crear_auto(request):
    auto = Auto(marca=random.choice(['Ford', 'Fiat', 'Chevrolet', 'Toyota']), modelo='Generico', anio=random.choice([2020, 2021, 2022, 2023, 2024]))
    auto.save()
    diccionario = {}
    return render(request, 'crear_auto.html', diccionario)