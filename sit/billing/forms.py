from django import forms
from core.models import Cliente, Producto
from .models import Factura, DetalleProductos, DetalleInsumos



class FacturaForm(forms.ModelForm):
    """
    Formulario para crear y editar facturas.

    Campos:
    Información de la factura:
        - numero_factura: Número único de la factura (clave primaria)
        - fecha_creacion: Fecha de creación de la factura
        - fecha_finalizacion: Fecha de finalización de la factura
        - fecha_entrega: Fecha de entrega de la factura
    Información de usuarios:
        - usuario_responsable: Usuario responsable de la factura
        - cliente: Cliente al que se le emite la factura
    Información de financiera:
        - valor_venta: Valor total de la venta
        - coste_servicio: Costo del servicio
    Información adicional:
        - adelanto: Adelanto realizado
        - valor_envio: Costo del envío
        - observaciones: Observaciones adicionales

    Atributos:
    - Meta: Clase que define el modelo asociado al formulario y los campos que
            se mostrarán en el formulario
    
    Métodos:
    - __init__: Constructor de la clase
    """
    class Meta:
        model = Factura
        fields = ['numero_factura', 'fecha_finalizacion', 
                  'fecha_entrega', 'usuario_responsable', 'cliente', 
                  'valor_venta', 'coste_insumos', 'coste_servicio', 'adelanto', 
                  'valor_envio', 'observaciones']
        widgets = {
            'fecha_finalizacion': forms.DateInput(attrs={'class': 'form-control', 
                                                         'type': 'date'}),
            'fecha_entrega': forms.DateInput(attrs={'class': 'form-control', 
                                                    'type': 'date'}),
            'usuario_responsable': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'valor_venta': forms.NumberInput(attrs={'class': 'form-control'}),
            'coste_servicio': forms.NumberInput(attrs={'class': 'form-control'}),
            'adelanto': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_envio': forms.NumberInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 
                                                   'rows': 3}),
        }
