from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class blogpost(models.Model):
    
    gen = models.CharField(max_length=64)
    fecha = models.DateField(null=False, blank=False)
    titulo = models.CharField(max_length=126)
    content = models.TextField(blank=False)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    def __str__ (self):
        return f"{self.creador} , {self.gen}, {self.fecha}, {self.titulo}, {self.content}"




