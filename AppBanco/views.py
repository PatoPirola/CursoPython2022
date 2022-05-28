from ast import Pass
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from AppBanco.forms import *
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User

# Create your views here.

def inicio(request):
    if request.user.is_authenticated:
        print("--------------> User is authenticated")
    return render(request,"AppBanco/inicio.html")

def clientes(request):

    if request.method == 'POST':
        formulario=ClienteForm(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            cliente = Clientes(codigo_cliente=informacion['codigo_cliente'], nombre=informacion['nombre'], email=informacion['email'])
            cliente.save()
            return render(request,"AppBanco/inicio.html")
    else:
        formulario=ClienteForm()
        return render(request,"AppBanco/clientes.html",{'formulario':formulario})

def buscar_cliente(request):
    return render(request,"AppBanco/busquedaCliente.html")

def buscar(request):
    if request.GET['codigo_cliente']:
        codigo_cliente=request.GET['codigo_cliente']
        cliente=Clientes.objects.filter(codigo_cliente=codigo_cliente)
        return render(request,"AppBanco/resultadoCliente.html",{'clientes':cliente})    
    else:
        respuesta="No se ingresó ningún código de cliente a buscar"
        return render(request,"AppBanco/resultadoCliente.html",{'respuesta':respuesta})
    
      
def productos(request):
    if request.method == 'POST':
        formulario=ProductoForm(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            cliente = Productos(codigo_producto=informacion['codigo_producto'], descripcion=informacion['descripcion'], subproducto=informacion['subproducto'])
            cliente.save()
            return render(request,"AppBanco/inicio.html")
    else:
        formulario=ProductoForm()
        return render(request,"AppBanco/productos.html",{'formulario':formulario})

def sucursales(request):
    if request.method == 'POST':
        formulario=SucursalForm(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            cliente = Sucursales(codigo_sucursal=informacion['codigo_sucursal'], sucursal=informacion['sucursal'], region=informacion['region'])
            cliente.save()
            return render(request,"AppBanco/inicio.html")
    else:
        formulario=SucursalForm()
        return render(request,"AppBanco/sucursales.html",{'formulario':formulario})


def login_view(request):
    if request.method == 'POST':
        formulario=LoginForm(request.POST)
        if formulario.is_valid():
            username=formulario.cleaned_data.get('username')
            password=formulario.cleaned_data.get('password')
            # Authenticate user      

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # A backend authenticated the credentials    
                print("Login successfuly")            
                # return render(request,"AppBanco/inicio.html")
                return inicio(request)
            else:
                # No backend authenticated the credentials       
                # Return an 'invalid login' error message.
                print("Login Failed")
                return render(request,"AppBanco/login.html", {'formulario':formulario})


    else:
        formulario=LoginForm()
        return render(request,"AppBanco/login.html", {'formulario':formulario})

def register(request):
    if request.method == 'POST':
        formulario=RegistrationForm(request.POST)
        if formulario.is_valid():
            username=formulario.cleaned_data.get('username')
            formulario.save()
            return render(request,"AppBanco/inicio.html", {'mensaje':"Usuario registrado con éxito"})

    else:
        formulario=RegistrationForm()


    return render(request,"AppBanco/registro.html", {'formulario':formulario})

def logout(request):
    logout(request)
    return render(request,"AppBanco/logout.html")
