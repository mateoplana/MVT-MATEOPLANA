from django.db import models

# Create your models here.

class familiar(models.Model):
    nombre=models.CharField(max_length=20)
    edad=models.IntegerField()
    fecha_de_nacimiento=models.DateField()