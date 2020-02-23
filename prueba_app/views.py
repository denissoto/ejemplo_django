from django.shortcuts import render
from prueba_app import models, forms
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy

# Esto es para la autenticación.
def auth_error(request):
	return render(request,'registration/login_auth.html')

#Las funciones de abajo son para validar a qué "grupo de usuario"
#pertenece el usuario que está logueado (que estás usando).

def in_clientes_group(user):
	av_groups = user.groups.all()
	for group in av_groups:
		if 'Clientes' in str(group):
			return True
	return False

def in_productos_group(user):
	av_groups = user.groups.all()
	for group in av_groups:
		if 'Productos' in str(group):
			return True
	return False

#A partir de acá son las funciones normales. La primera clase va a ser
#la de la página de inicio, que me va a mostrar datos de las dos tablas,
#clientes y usuarios.

class inicio(generic.ListView):
    template_name= 'inicio.html'
    def get_context_data(self,**kwargs):
        context = super(inicio, self).get_context_data(**kwargs)
        context.update({
            'clientes': models.clientes.objects.all(),
			'productos': models.productos.objects.all(),
        })
        return context
    def get_queryset(self):
        return models.clientes.objects

class clientes(generic.ListView):
    template_name= 'clientes.html'
    def get_context_data(self,**kwargs):
        context = super(clientes, self).get_context_data(**kwargs)
        context.update({
            'clientes': models.clientes.objects.all()
        })
        return context
    def get_queryset(self):
        return models.clientes.objects

class productos(generic.ListView):
    template_name= 'productos.html'
    def get_context_data(self,**kwargs):
        context = super(productos, self).get_context_data(**kwargs)
        context.update({
            'productos': models.productos.objects.all()
        })
        return context
    def get_queryset(self):
        return models.productos.objects

@method_decorator(user_passes_test(in_clientes_group, login_url='auth_error'),name='dispatch')
class clientes_crear(generic.CreateView):
    template_name= 'crea_clientes.html'
    form_class= forms.clientes
    success_url = reverse_lazy('clientes')

@method_decorator(user_passes_test(in_productos_group, login_url='auth_error'),name='dispatch')
class productos_crear(generic.CreateView):
    template_name= 'crea_productos.html'
    form_class= forms.productos
    success_url = reverse_lazy('productos')