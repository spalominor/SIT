from django import forms
from .models import Cliente, Producto, Insumo



class ClienteForm(forms.ModelForm):
    """
    Formulario de cliente. Aquí se definen los campos que se mostrarán en el
    formulario de cliente.

    Campos:
    - nombre: Nombre del cliente
    - celular: Número de celular del cliente
    - direccion: Dirección del cliente
    - observaciones: Observaciones adicionales sobre el cliente

    Atributos:
    - Meta: Clase que define el modelo asociado al formulario y los campos que
            se mostrarán en el formulario
    
    Métodos:
    - __init__: Constructor de la clase
    """
    class Meta:
        model = Cliente
        fields = ['nombre', 'celular', 'direccion', 'observaciones']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 
                                               'rows': 3}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 
                                                   'rows': 2}),
        }


class ProductoForm(forms.ModelForm):
    """
    Formulario de producto. Aquí se definen los campos que se mostrarán en el
    formulario de producto.

    Campos:
    - nombre: Nombre del producto
    - precio: Precio del producto
    - descripcion: Descripción del producto
    - stock: Cantidad de stock del producto

    Atributos:
    - Meta: Clase que define el modelo asociado al formulario y los campos que
            se mostrarán en el formulario

    Métodos:
    - __init__: Constructor de la clase
    """
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'stock']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control',
                                                 'rows': 3}),
            'stock': forms.TextInput(attrs={'class': 'form-control'}),
        }

    
class InsumoForm(forms.ModelForm):
    """
    Formulario de insumo. Aquí se definen los campos que se mostrarán en el
    formulario de insumo.

    Campos:
    - nombre: Nombre del insumo
    - cantidad: Cantidad del insumo
    - precio: Precio del insumo
    - descripcion: Descripción del insumo
    - stock: Cantidad de stock del insumo

    Atributos:
    - Meta: Clase que define el modelo asociado al formulario y los campos que
            se mostrarán en el formulario

    Métodos:
    - __init__: Constructor de la clase
    """
    class Meta:
        model = Insumo
        fields = ['nombre', 'cantidad', 'precio', 'descripcion', 'stock']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control',
                                                 'rows': 3}),
            'stock': forms.TextInput(attrs={'class': 'form-control'}),
        }