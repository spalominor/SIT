from django.db import models



class Cliente(models.Model):
    """
    Modelo de cliente. Aquí se almacenan los datos de los clientes de la
    empresa. 
    Los campos son:
    - id: Identificador único del cliente (clave primaria)
    - nombre: Nombre del cliente
    - celular: Número de celular del cliente
    - direccion: Dirección del cliente
    - observaciones: Observaciones adicionales sobre el cliente

    Atributos:
    - id: Identificador único del cliente
    - nombre: Nombre del cliente
    - celular: Número de celular del cliente
    - direccion: Dirección del cliente
    - observaciones: Observaciones adicionales sobre el cliente

    Métodos:
    - __str__: Representación amigable del cliente
    """
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    celular = models.CharField(max_length=10)
    direccion = models.TextField(max_length=100)
    observaciones = models.TextField(blank=True, null=True, max_length=1000)

    def __str__(self):
        """
        Este método devuelve una representación amigable del cliente.
        """
        return self.nombre
    

class Producto(models.Model):
    """
    Modelo de producto. Aquí se almacenan los datos de los productos de la
    empresa.

    Atributos:
    - id: Identificador único del producto
    - nombre: Nombre del producto
    - tipo: Tipo de producto (cuello, fajón, puño, otro)
    - descripcion: Descripción del producto
    - precio_base: Precio base del producto
    - stock: Cantidad de productos en stock
    - activo: Indica si el producto está disponible

    Métodos:
    - __str__: Representación amigable del producto
    """
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(
        max_length=20,
        choices=[
            ('cuello', 'Cuello'),
            ('fajon', 'Fajón'),
            ('puno', 'Puño'),
            ('bordado', 'Bordado'),
            ('laser', 'Láser'),
            ('otro', 'Otro'),
        ],
        default='cuello',
    )
    descripcion = models.TextField(blank=True, null=True)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)  # Opcional: para controlar la disponibilidad

    def __str__(self):
        """
        Este método devuelve una representación amigable del producto.

        Args:
            None

        Returns:
            str: Representación amigable del producto
            Ejemplo: "Cuello (cuello - $10.00)"
        """
        return f"{self.nombre} ({self.tipo} - ${self.precio_base})"
    

class Insumo(models.Model):
    """
    Modelo de insumos. Aquí se almacenan los datos de los insumos de la
    empresa.

    Atributos:
    - id: Identificador único del insumo
    - nombre: Nombre del insumo
    - descripcion: Descripción del insumo
    - stock: Cantidad de insumos en stock
    - activo: Indica si el insumo está disponible

    Métodos:
    - __str__: Representación amigable del insumo
    """
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)  # Opcional: para controlar la disponibilidad

    def __str__(self: "Insumo") -> str:
        """
        Este método devuelve una representación amigable del insumo.

        Args:
            None

        Returns:
            str: Representación amigable del insumo
            Ejemplo: "Tela de algodón"
        """
        return self.nombre