from django.http import HttpResponse
from django.shortcuts import render

from .models import Destino, Hotel, Sitios_para_visitar, Recomendacion
from AppViaje.forms import Destinoformulario
from AppViaje.forms import Hotelformulario
from AppViaje.forms import Recomendacionformulario
from AppViaje.forms import Sitios_para_visitar_formulario

# Create your views here.

def inicio(request):
    return render (request, "AppViaje/inicio.html")

def destino(request):
    return render (request, "AppViaje/destino.html")

def hotel(request):
    return render (request, "AppViaje/hotel.html")

def sitios_para_visitar(request):
    return render (request, "AppViaje/sitiosparavisitar.html")

def recomendacion(request):
    return render (request, "AppViaje/recomendacion.html")

"""
view para formulario a mano
def destinoformulario(request):

    if request.method=="POST":
        pais=request.POST.get("pais")
        ciudad=request.POST.get("ciudad")
        destino=Destino(pais=pais,ciudad=ciudad)
        destino.save()
        return render(request, "AppViaje/inicio.html")
    return render (request, "AppViaje/destinoformulario.html")"""

def destinoformulario(request):

    if request.method=="POST":
        miFormulario= Destinoformulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            print(info)
            pais=info.get("pais")
            ciudad=info.get("ciudad")
            destino=Destino(pais=pais,ciudad=ciudad)
            destino.save()
            return render(request, "AppViaje/inicio.html", {"mensaje": "Destino creado"})
        else:
            return render(request, "AppViaje/inicio.html", {"mensaje": "Error"})
    
    else:
        miFormulario=Destinoformulario()
        return render(request, "AppViaje/destinoformulario.html", {"formulario":miFormulario})

def hotelformulario(request):

    if request.method=="POST":
        form= Hotelformulario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            precio_por_noche=info["preciopornoche"]
            hotel=Hotel(nombre=nombre,preciopornoche=precio_por_noche)
            hotel.save()
            return render(request, "AppViaje/inicio.html", {"mensaje": "Hotel creado"})
        else:
            return render(request, "AppViaje/inicio.html", {"mensaje": "Error"})
    
    else:
        form=Hotelformulario()
        return render(request, "AppViaje/hotelformulario.html", {"formulario":form})

def recomendacionformulario(request):

    if request.method=="POST":
        formm= Recomendacionformulario(request.POST)
        if formm.is_valid():
            inf=formm.cleaned_data
            comentarios=inf["comentarios"]
            recomendacion=Recomendacion(comentarios=comentarios)    
            recomendacion.save()
            return render(request, "AppViaje/inicio.html", {"mensaje": "Recomendacion creada"})
        else:
            return render(request, "AppViaje/inicio.html", {"mensaje": "Error"})
    
    else:
        formm=Recomendacionformulario()
        return render(request, "AppViaje/recomendacionformulario.html", {"formulario":formm})

def sitiosparavisitarformulario(request):

    if request.method=="POST":
        formmm= Sitios_para_visitar_formulario(request.POST)    
        if formmm.is_valid():
            infor=formmm.cleaned_data
            nombre=infor["nombre"]
            horario=infor["horario"]
            sitiosparavisitar=Sitios_para_visitar_formulario(nombre=nombre, horario=horario)    
            sitiosparavisitar.save()
            return render(request, "AppViaje/inicio.html", {"mensaje": "Recomendacion creada"})
        else:
            return render(request, "AppViaje/inicio.html", {"mensaje": "Error"})
    
    else:
        formmm=Sitios_para_visitar_formulario()
        return render(request, "AppViaje/sitiosparavisitarformulario.html", {"formulario":formmm})

def busquedaCiudad(request):
    return render(request, "AppViaje/busquedaCiudad.html")

def buscar(request):
    if request.GET["ciudad"]:
        ciudad=request.GET.get("ciudad")
        destino=Destino.objects.filter(ciudad=ciudad)
        if len(destino)!=0:
            return render(request, "AppViaje/resultadosbusqueda.html", {"ciudad":ciudad})
        else:
            return render(request, "AppViaje/resultadosbusqueda.html", {"mensaje":"No se encontró la ciudad"})
    else:
        return render(request, "AppViaje/resultadosbusqueda.html", {"mensaje":"No enviaste datos"})