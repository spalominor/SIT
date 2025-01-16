from django.db import models
from django.contrib.auth.models import User  
from core.models import Cliente
from decimal import Decimal



class Factura(models.Model):
    """
    Modelo de factura. Aquí se almacenan los datos de las facturas de la
    empresa. 

    Atributos:
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
        - coste_insumos: Costo total de insumos
        - coste_servicio: Costo del servicio
    Información adicional:
        - adelanto: Adelanto realizado
        - valor_envio: Costo del envío
        - observaciones: Observaciones adicionales

    Métodos:
    - __str__: Representación amigable de la factura
    """
    # Información de la factura
    numero_factura = models.AutoField(primary_key=True)  # Campo único para cada factura
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha automática al crear
    fecha_finalizacion = models.DateTimeField(blank=True, null=True)  # Se llenará manualmente
    fecha_entrega = models.DateTimeField(blank=True, null=True)  # Se llenará manualmente

    # Información de usuarios
    usuario_responsable = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Relación con el cliente

    # Información financiera
    valor_venta = models.DecimalField(max_digits=10, decimal_places=2)  # Valor total de la venta
    coste_insumos = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Costo total de insumos
    coste_servicio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Costo del servicio

    # Información adicional
    adelanto = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Adelanto realizado
    valor_envio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Costo del envío
    observaciones = models.TextField(blank=True, null=True, max_length=1000)  # Observaciones adicionales

    def __str__(self):
        """
        Este método devuelve una representación amigable de la factura.

        Args:
            None

        Returns:
            str: Representación amigable de la factura
            Ejemplo: "Factura 1 - Cliente: Juan Pérez"
        """
        return f"Factura {self.numero_factura} - Cliente: {self.cliente.nombre}"
    

class DetalleProductos(models.Model):
    """
    Este modelo representa un detalle de la factura. Aquí se almacenan los
    productos que se incluyen en la factura.

    Atributos:
    - id: Identificador único del detalle de la factura
    - factura: Factura a la que pertenece el detalle
    - producto: Nombre del producto
    - cantidad: Cantidad de productos
    - precio_unitario: Precio unitario del producto

    Métodos:
    - __str__: Representación amigable del detalle de la factura
    - total_producto: Total del producto en el detalle
    """
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name="detalleProducto")
    producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self: "DetalleProductos") -> str:
        """
        Este método devuelve una representación amigable del detalle de la 
        factura.

        Args:
            None

        Returns:
            str: Representación amigable del detalle de la factura
            Ejemplo: "Pedido 1 - Cuello (x2)"
        """
        return f"Pedido {self.id} - {self.producto} (x{self.cantidad})"

    @property
    def total_producto(self: "DetalleProductos") -> Decimal:
        """
        Este método calcula el total de un producto en el detalle de la factura

        Args:
            None
        
        Returns:
            Decimal: Total del producto
        """
        return self.cantidad * self.precio_unitario
    

class DetalleInsumos(models.Model):
    """
    Este modelo representa un detalle de la factura. Aquí se almacenan los
    insumos que se incluyen en la factura.

    Atributos:
    - id: Identificador único del detalle de la factura
    - factura: Factura a la que pertenece el detalle
    - insumo: Nombre del insumo
    - cantidad: Cantidad de insumos
    - precio_unitario: Precio unitario del insumo

    Métodos:
    - __str__: Representación amigable del detalle de la factura
    - total_insumo: Total del insumo en el detalle
    """
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name="detalleFactura")
    insumo = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self: "DetalleInsumos") -> str:
        """
        Este método devuelve una representación amigable del detalle de la
        factura.

        Args:
            None

        Returns:
            str: Representación amigable del detalle de la factura
            Ejemplo: "Pedido 1 - Cuello (x2)"
        """
        return f"Pedido {self.id} - {self.insumo} (x{self.cantidad})"

    @property
    def total_insumo(self: "DetalleInsumos") -> Decimal:
        """
        Este método calcula el total de un insumo en el detalle de la factura

        Args:
            None

        Returns:
            Decimal: Total del insumo
        """
        return self.cantidad * self.precio_unitario