from django.db import models

# Create your models here.

class Destino(models.Model):
    pais=models.CharField(max_length=50)
    ciudad=models.CharField(max_length=50)

    def __str__(self):
        return self.pais+" "+str(self.ciudad)

class Hotel(models.Model):
    nombre=models.CharField(max_length=50)
    precio_por_noche=models.IntegerField()

class Sitios_para_visitar(models.Model):
    nombre=models.CharField(max_length=50)
    horario=models.CharField(max_length=50)

class Recomendacion(models.Model):
    comentarios=models.CharField(max_length=300)
    