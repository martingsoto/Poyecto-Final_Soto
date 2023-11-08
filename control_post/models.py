from django.db import models

# Create your models here.

class usuario(models.Model):
    usuario = models.CharField(max_length=64)
    contra = models.CharField(max_length=12)
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    dni = models.IntegerField()
    email = models.EmailField(blank=True)
    



class genero(models.Model):
    nombre = models.CharField(max_length=64)
    cantidad = models.IntegerField()


class posteo(models.Model):
    autor = usuario
    fecha = models.DateField(null=False, blank=False)
    titulo = models.CharField()
    content = models.TextField(blank=False)




