from django.db import models

# Create your models here.

class Familiares (models.Model):
    Nombres = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=50)
    Con_Vida = models.BooleanField()
    Hijos = models.IntegerField()
    
