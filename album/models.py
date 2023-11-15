from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.
class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    celular = models.IntegerField()
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('profesor-list')

class Materia(models.Model):
    nombre = models.CharField(max_length=50)
    profesor = models.ForeignKey('Profesor', on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('materia-list')

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    celular = models.IntegerField()
    direccion = models.CharField(max_length=50)
    materia = models.ForeignKey('Materia', on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('materia-list')
