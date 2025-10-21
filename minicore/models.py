from django.db import models

class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}"

class Reglas(models.Model):
    nombre = models.CharField(max_length=100)
    monto_min = models.DecimalField(max_digits=10, decimal_places=2)
    monto_max = models.DecimalField(max_digits=10, decimal_places=2)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, related_name='ventas')
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.vendedor.nombre} - {self.fecha} - ${self.monto}"