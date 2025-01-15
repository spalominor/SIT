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
        # Representación amigable del cliente
        return self.nombre