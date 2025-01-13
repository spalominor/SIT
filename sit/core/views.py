from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from . import models



def crear_cliente(request):
    """
    Vista para crear un cliente. 
    Si el método es POST, se intenta guardar el cliente en la base de datos.
    Si el formulario es válido, se guarda el cliente y se redirige a la lista
    de clientes.
    Si el método es GET, se muestra el formulario vacío para crear un cliente.
    
    Argumentos:
    - request: HttpRequest con la información de la solicitud HTTP actual.
    
    Returns: 
    - HttpResponse con la respuesta HTTP.
    """
    if request.method == 'POST':
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente creado exitosamente.")
            return redirect('listar_clientes')  
    else:
        form = forms.ClienteForm()
    return render(request, 'core/crear_cliente.html', {'form': form})


def listar_clientes(request):
    """
    Vista para listar los clientes de la empresa.
    Se obtienen todos los clientes de la base de datos y se pasan al template
    para ser mostrados.
    
    Argumentos:
    - request: HttpRequest con la información de la solicitud HTTP actual.
    
    Returns:
    - HttpResponse con la respuesta HTTP.
    """
    clientes = models.Cliente.objects.all()
    return render(request, 'core/listar_clientes.html', {'clientes': clientes})


def editar_cliente(request, cliente_id):
    """
    Vista para editar un cliente.
    Si el método es POST, se intenta actualizar el cliente en la base de datos.
    Si el formulario es válido, se guarda el cliente y se redirige a la lista
    de clientes.
    Si el método es GET, se muestra el formulario con los datos del cliente
    para ser editados.
    
    Argumentos:
    - request: HttpRequest con la información de la solicitud HTTP actual.
    
    Returns:
    - HttpResponse con la respuesta HTTP.
    """
    cliente = models.Cliente.objects.get(id=cliente_id)
    if request.method == 'POST':
        if 'update' in request.POST:  
            # Si el usuario desea actualizar
            form = forms.ClienteForm(request.POST, instance=cliente)
            if form.is_valid():
                form.save()
                return redirect('listar_clientes')
        elif 'delete' in request.POST:
            # Si el usuario desea eliminar
            cliente.delete()
            return redirect('listar_clientes')
    else:
        form = forms.ClienteForm(instance=cliente)
    return render(request, 'core/editar_cliente.html', 
                  {'form': form, 'cliente': cliente})

