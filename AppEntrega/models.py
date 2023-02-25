from django.db import models

# Create your models here.
class Proveedores(models.Model):
    empresa = models.CharField(max_length=30)
    cuit = models.IntegerField()
    localidad = models.CharField(max_length=50)
    def __str__(self) -> str:
        return (self.empresa)

class Vendedores(models.Model):
    nombre = models.CharField(max_length=30)
    dni = models.IntegerField()
    activo_actualmente = models.BooleanField()
    def __str__(self) -> str:
        return (self.nombre)

class Productos(models.Model):
    sku = models.IntegerField()
    descripcion = models.CharField(max_length=30)
    fecha_de_carga = models.DateField()
    disponibilidad = models.BooleanField()
    def __str__(self) -> str:
        return (f"{self.sku} - {self.descripcion}")

    

