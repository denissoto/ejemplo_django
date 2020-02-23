from django.db import models

# Create your models here.

class clientes(models.Model):
  nombre= models.CharField(max_length=50)
  apellido= models.CharField(max_length=50)
  documento= models.CharField(max_length=50)
  def __str__(self):
    return '{0} {1}'.format(self.nombre, self.apellido)

class productos(models.Model):
  codigo= models.CharField(max_length=50)
  descripcion= models.CharField(max_length=50)
  precio= models.CharField(max_length=50)
  def __str__(self):
    return '{0} - {1}'.format(self.codigo, self.descripcion)