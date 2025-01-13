from django import forms
from .models import Cliente



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
