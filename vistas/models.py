from django.db import models 
from django.db.models.deletion import CASCADE 

# Create your models here.



class Carac_moviles(models.Model):
    nombre=models.CharField(max_length=50)
    ram=models.CharField(max_length=50)
    tamaño=models.CharField(max_length=50)
    capacidad=models.CharField(max_length=50)
    mpx_camara=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="moviles")
    precio=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre



class Fundas(models.Model):
    nombre=models.CharField(max_length=50)
    movil=models.ForeignKey(Carac_moviles, on_delete=models.CASCADE)
    color=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="moviles")
    precio=models.CharField(max_length=50)


    def __str__(self):
        return self.nombre


class Protector(models.Model):
    nombre=models.CharField(max_length=50)
    movil=models.ForeignKey(Carac_moviles, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="moviles")
    precio=models.CharField(max_length=50)


    def __str__(self):
        return self.nombre









