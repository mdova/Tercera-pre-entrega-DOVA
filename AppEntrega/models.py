from django.db import models

# Create your models here.
class Proveedores(models.Model):
    empresa = models.CharField(max_length=30)
    cuit = models.IntegerField()
    localidad = models.CharField(max_length=50)

class Vendedores(models.Model):
    nombre = models.CharField(max_length=30)
    dni = models.IntegerField()
    activo_actualmente = models.BooleanField()

class Productos(models.Model):
    sku = models.IntegerField()
    marca = models.CharField(max_length=30)
    tipo = models.CharField(max_length=50)
    disponibilidad = models.BooleanField(default=True)

    

