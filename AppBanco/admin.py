from django.contrib import admin

from AppBanco.models import Clientes, Productos, Sucursales

# Register your models here.

admin.site.register(Clientes)
admin.site.register(Productos)
admin.site.register(Sucursales)