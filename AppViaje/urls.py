from django.urls import path
from .views import *

urlpatterns=[
    path('destino/', destino, name='destino'),
    path('hotel/', hotel, name='hotel'),
    path('sitiosparavisitar/', sitios_para_visitar, name='sitiosparavisitar'),
    path('recomendacion/', recomendacion, name='recomendacion'),
    path('inicio/', inicio, name='inicio'),
    path('destinoformulario/', destinoformulario, name='destinoformulario'),
    path('hotelformulario/', hotelformulario, name='hotelformulario'),
    path('recomendacionformulario/', recomendacionformulario, name='recomendacionformulario'),
    path('sitiosparavisitarformulario/', sitiosparavisitarformulario, name='sitiosparavisitarformulario'),
    path('busquedaCiudad/', busquedaCiudad, name='busquedaCiudad'),
    path('buscar/', buscar, name='buscar'),
]