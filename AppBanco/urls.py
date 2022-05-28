from django.urls import path
from .views import * 
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',inicio,name='inicio'),
    path('login/', login_view,name='login'),
    path('registro/', register,name='register'),
    path('logout/', LogoutView.as_view(template_name='AppBanco/logout.html'),name='logout'),
    path('clientes/', clientes,name='clientes'),
    path('productos/', productos,name='productos'),
    path('sucursales/', sucursales,name='sucursales'),
    path('buscar_cliente/',buscar_cliente,name='buscar_cliente'),
    path('buscar/',buscar,name='buscar'),
]