from django.shortcuts import render, redirect
from django.contrib import messages
import core.forms as coreForms
import core.models as coreModels
from . import forms
from . import models



def registrar_cliente(request):
    if request.method == 'POST':
        cliente_form = coreForms.ClienteForm(request.POST)
        if cliente_form.is_valid():
            # Guardar datos del cliente en la sesión
            cliente_data = cliente_form.cleaned_data
            request.session['cliente_data'] = cliente_data
            return redirect('crear_factura_productos')
    else:
        cliente_form = coreForms.ClienteForm()

    return render(request, 'billing/registrar_cliente.html', 
                  {'form': cliente_form})


def registrar_productos(request):
    if request.method == 'POST':
        producto_form = coreForms.ProductoForm(request.POST)
        if producto_form.is_valid():
            # Agregar producto a la lista de productos en la sesión
            productos = request.session.get('productos', [])
            productos.append(producto_form.cleaned_data)
            request.session['productos'] = productos
            return redirect('crear_factura_insumos')  # O redirigir al mismo paso para añadir más productos
    else:
        producto_form = coreForms.ProductoForm()

    return render(request, 'billing/registrar_productos.html', {'form': producto_form})


def registrar_insumos(request):
    if request.method == 'POST':
        insumo_form = coreForms.InsumoForm(request.POST)
        if insumo_form.is_valid():
            # Agregar insumo a la lista de insumos en la sesión
            insumos = request.session.get('insumos', [])
            insumos.append(insumo_form.cleaned_data)
            request.session['insumos'] = insumos
            return redirect('crear_factura_coste')  # O redirigir al mismo paso para añadir más insumos
    else:
        insumo_form = coreForms.InsumoForm()

    return render(request, 'billing/registrar_insumos.html', {'form': insumo_form})


def registrar_coste_servicio(request):
    if request.method == 'POST':
        coste_servicio = request.POST.get('coste_servicio')
        if coste_servicio:
            request.session['coste_servicio'] = float(coste_servicio)
            return redirect('crear_factura_adelanto')

    return render(request, 'billing/registrar_coste_servicio.html')


def registrar_adelanto(request):
    if request.method == 'POST':
        adelanto = request.POST.get('adelanto')
        if adelanto:
            request.session['adelanto'] = float(adelanto)
            return redirect('crear_factura_observaciones')

    return render(request, 'billing/registrar_adelanto.html')


def registrar_observaciones(request):
    if request.method == 'POST':
        observaciones = request.POST.get('observaciones')
        request.session['observaciones'] = observaciones
        return redirect('finalizar_factura')

    return render(request, 'billing/registrar_observaciones.html')


def finalizar_factura(request):
    cliente_data = request.session.get('cliente_data')
    productos = request.session.get('productos', [])
    insumos = request.session.get('insumos', [])
    coste_servicio = request.session.get('coste_servicio', 0)
    adelanto = request.session.get('adelanto', 0)
    observaciones = request.session.get('observaciones', '')

    if request.method == 'POST':
        # Crear el cliente
        cliente = coreModels.Cliente.objects.create(**cliente_data)

        # Crear la factura
        factura = models.Factura.objects.create(
            usuario_responsable=request.user,
            cliente=cliente,
            valor_venta=sum(p['precio_base'] * p['cantidad'] for p in productos),
            coste_insumos=sum(i['precio_base'] * i['cantidad'] for i in insumos),
            coste_servicio=coste_servicio,
            adelanto=adelanto,
            observaciones=observaciones
        )

        # Crear los detalles de productos
        for producto in productos:
            models.DetalleProductos.objects.create(
                factura=factura,
                producto=producto['nombre'],
                cantidad=producto['cantidad'],
                precio_unitario=producto['precio_base']
            )

        # Crear los detalles de insumos
        for insumo in insumos:
            models.DetalleInsumos.objects.create(
                factura=factura,
                insumo=insumo['nombre'],
                cantidad=insumo['cantidad'],
                precio_unitario=insumo['precio_base']
            )

        # Limpiar la sesión
        request.session.flush()

        # Redirigir a un detalle de factura o página de éxito
        return redirect('detalle_factura', factura_id=factura.pk)

    return render(request, 'billing/finalizar_factura.html', {
        'cliente_data': cliente_data,
        'productos': productos,
        'insumos': insumos,
        'coste_servicio': coste_servicio,
        'adelanto': adelanto,
        'observaciones': observaciones,
    })


def detalle_factura(request, factura_id):
    factura = models.Factura.objects.get(pk=factura_id)
    detalles_productos = models.DetalleProductos.objects.filter(factura=factura)
    detalles_insumos = models.DetalleInsumos.objects.filter(factura=factura)

    return render(request, 'billing/detalle_factura.html', {
        'factura': factura,
        'detalles_productos': detalles_productos,
        'detalles_insumos': detalles_insumos,
    })


def buscar_cliente(request):
    query = request.GET.get('q')
    resultados = coreModels.Cliente.objects.filter(nombre__icontains=query) if query else None
    return render(request, 'billing/registrar_cliente.html', {'resultados_clientes': resultados})


def buscar_producto(request):
    query = request.GET.get('q')
    resultados = coreModels.Producto.objects.filter(nombre__icontains=query) if query else None
    return render(request, 'facturas/registrar_productos.html', {'resultados_productos': resultados})


def buscar_insumo(request):
    query = request.GET.get('q')
    resultados = coreModels.Insumo.objects.filter(nombre__icontains=query) if query else None
    return render(request, 'facturas/registrar_insumos.html', {'resultados_insumos': resultados})