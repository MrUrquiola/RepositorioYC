from datetime import datetime
from django.template import Template, Context
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola mundo")

def segunda_vista(request):
    return HttpResponse("Ya entendi! esto es muy simple!!!")

def dia_de_hoy(request):
    dia=datetime.today()
    cadena="Hoy es "+str(dia)
    return HttpResponse(cadena)

def saludo_con_nombre(request, nombre):
    return HttpResponse("<h1>Hola mi nombre es: "+nombre+"</h1>")

def calcula_anio_nacimiento(request, edad):
    anio_nacimiento=2022-int(edad)
    return HttpResponse("<h1>Tu año de nacimiento es: "+str(anio_nacimiento)+"</h1>")

def probandohtml(request):

    nom="CeYe"
    ape="UrquiMar"
    edad=22
    lista_notas=[9,9,8,7,8,9]
    diccionario={'nombre': nom, 'apellido': ape, 'edad': edad, 'lista': lista_notas}

    mihtml= open("C:/Users/A308123/OneDrive - Santander Office 365/Escritorio/ProyectoFinalYC/ProyectoYC/Plantillas/template1.html")
    plantilla=Template(mihtml.read())
    mihtml.close()
    Contexto= Context(diccionario)
    documento=plantilla.render(Contexto)
    return HttpResponse(documento)
