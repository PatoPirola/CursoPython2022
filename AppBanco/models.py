import email
from mailbox import NoSuchMailboxError
from django.db import models

# Create your models here.
class Clientes(models.Model):
    codigo_cliente=models.IntegerField()
    nombre=models.CharField(max_length=40)
    email=models.EmailField()

    def __str__(self):
        return self.nombre

class Productos(models.Model):
    codigo_producto=models.IntegerField()
    descripcion=models.CharField(max_length=40)
    subproducto=models.CharField(max_length=40)

    def __str__(self):
        return self.codigo_producto

class Sucursales(models.Model):
    codigo_sucursal=models.IntegerField()
    sucursal=models.CharField(max_length=40)
    region=models.CharField(max_length=20)

    def __str__(self):
        return self.sucursal