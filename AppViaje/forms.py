from django import forms

class Destinoformulario(forms.Form):
    pais=forms.CharField(max_length=50)
    ciudad=forms.CharField(max_length=50)

class Hotelformulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    precio_por_noche=forms.CharField(max_length=50)

class Sitios_para_visitar_formulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    horario=forms.CharField(max_length=50)

class Recomendacionformulario(forms.Form):
    comentarios=forms.CharField(max_length=300)

