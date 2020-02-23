from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from prueba_app import views

urlpatterns = [
    path('', login_required(views.inicio.as_view()), name='inicio'),
    path('auth_error',views.auth_error, name='auth_error'),
    path('admin/', admin.site.urls),
    path('clientes', views.clientes.as_view(), name='clientes'),
    path('productos', views.productos.as_view(), name='productos'),
    path('clientes_crear', views.clientes_crear.as_view(), name='clientes_crear'),
    path('productos_crear', views.productos_crear.as_view(), name='productos_crear'),
    ]