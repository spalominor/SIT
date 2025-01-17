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
                messages.warning(request, "Cliente actualizado exitosamente.")
                return redirect('listar_clientes')
        elif 'delete' in request.POST:
            # Si el usuario desea eliminar
            cliente.delete()
            messages.warning(request, "Cliente eliminado exitosamente.")
            return redirect('listar_clientes')
    else:
        form = forms.ClienteForm(instance=cliente)
    return render(request, 'core/editar_cliente.html', 
                  {'form': form, 'cliente': cliente})


def crear_producto(request):
    """
    Vista para crear un producto. 
    Si el método es POST, se intenta guardar el producto en la base de datos.
    Si el formulario es válido, se guarda el producto y se redirige a la lista
    de productos.
    Si el método es GET, se muestra el formulario vacío para crear un producto.
    
    Argumentos:
    - request: HttpRequest con la información de la solicitud HTTP actual.
    
    Returns: 
    - HttpResponse con la respuesta HTTP.
    """
    if request.method == 'POST':
        form = forms.ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto creado exitosamente.")
            return redirect('listar_productos')  
    else:
        form = forms.ProductoForm()
    return render(request, 'core/crear_producto.html', {'form': form})


def listar_productos(request):
    """
    Vista para listar los productos de la empresa.
    Se obtienen todos los productos de la base de datos y se pasan al template
    para ser mostrados.
    
    Argumentos:
    - request: HttpRequest con la información de la solicitud HTTP actual.
    
    Returns:
    - HttpResponse con la respuesta HTTP.
    """
    productos = models.Producto.objects.all()
    return render(request, 'core/listar_productos.html', 
                  {'productos': productos})


def editar_producto(request, producto_id):
    """
    Vista para editar un producto.
    Si el método es POST, se intenta actualizar el producto en la base de datos
    Si el formulario es válido, se guarda el producto y se redirige a la lista
    de productos.
    Si el método es GET, se muestra el formulario con los datos del producto
    para ser editados.
    
    Argumentos:
    - request: HttpRequest con la información de la solicitud HTTP actual.
    
    Returns:
    - HttpResponse con la respuesta HTTP.
    """
    producto = models.Producto.objects.get(id=producto_id)
    if request.method == 'POST':
        if 'update' in request.POST:  
            # Si el usuario desea actualizar
            form = forms.ProductoForm(request.POST, instance=producto)
            if form.is_valid():
                producto = form.save(commit=False)
                # Verificar si se ha mandado un valor 'activo' en el formulario
                producto.activo = 'activo' in request.POST
                form.save()
                messages.warning(request, "Producto actualizado exitosamente.")
                return redirect('listar_productos')
        elif 'delete' in request.POST:
            # Si el usuario desea eliminar
            producto.delete()
            return redirect('listar_productos')
    else:
        form = forms.ProductoForm(instance=producto)
    return render(request, 'core/editar_producto.html', 
                  {'form': form, 'producto': producto})


def crear_insumo(request):
    """
    Vista para crear un insumo.
    Si el método es POST, se intenta guardar el insumo en la base de datos.
    Si el formulario es válido, se guarda el insumo y se redirige a la lista
    de insumos.
    Si el método es GET, se muestra el formulario vacío para crear un insumo.

    Argumentos:
    - request: HttpRequest con la información de la solicitud HTTP actual.

    Returns:
    - HttpResponse con la respuesta HTTP.
    """
    if request.method == 'POST':
        form = forms.InsumoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Insumo creado exitosamente.")
            return redirect('listar_insumos')
    else:
        form = forms.InsumoForm()
    return render(request, 'core/crear_insumo.html', {'form': form})


def listar_insumos(request):
    """
    Vista para listar los insumos de la empresa.
    Se obtienen todos los insumos de la base de datos y se pasan al template
    para ser mostrados.

    Argumentos:
    - request: HttpRequest con la información de la solicitud HTTP actual.

    Returns:
    - HttpResponse con la respuesta HTTP.
    """
    insumos = models.Insumo.objects.all()
    return render(request, 'core/listar_insumos.html', {'insumos': insumos})


def editar_insumo(request, insumo_id):
    """
    Vista para editar un insumo.
    Si el método es POST, se intenta actualizar el insumo en la base de datos.
    Si el formulario es válido, se guarda el insumo y se redirige a la lista
    de insumos.
    Si el método es GET, se muestra el formulario con los datos del insumo
    para ser editados.

    Argumentos:
    - request: HttpRequest con la información de la solicitud HTTP actual.

    Returns:
    - HttpResponse con la respuesta HTTP.
    """
    insumo = models.Insumo.objects.get(id=insumo_id)
    if request.method == 'POST':
        if 'update' in request.POST:
            # Si el usuario desea actualizar
            form = forms.InsumoForm(request.POST, instance=insumo)
            if form.is_valid():
                insumo = form.save(commit=False)
                # Verificar si se ha mandado un valor 'activo' en el formulario
                insumo.activo = 'activo' in request.POST
                form.save()
                messages.warning(request, "Insumo actualizado exitosamente.")
                return redirect('listar_insumos')
        elif 'delete' in request.POST:
            # Si el usuario desea eliminar
            insumo.delete()
            return redirect('listar_insumos')
    else:
        form = forms.InsumoForm(instance=insumo)
    return render(request, 'core/editar_insumo.html',
                  {'form': form, 'insumo': insumo})