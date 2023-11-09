from django.db import models

# Create your models here.

class usuario(models.Model):
    logname = models.CharField(max_length=64)
    contra = models.CharField(max_length=12)
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    dni = models.IntegerField()
    email = models.EmailField(blank=True)
    



class genero(models.Model):
    nombre = models.CharField(max_length=64)
    cantidad = models.IntegerField()


class blogpost(models.Model):
    autor = models.CharField(max_length=64)
    gen = models.CharField(max_length=64)
    fecha = models.DateField(null=False, blank=False)
    titulo = models.CharField(max_length=126)
    content = models.TextField(blank=False)




