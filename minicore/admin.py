from django.contrib import admin
from .models import Vendedor, Venta
from .models import Reglas

@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


@admin.register(Reglas)
class ReglaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'monto_min', 'monto_max', 'porcentaje')

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'vendedor', 'fecha', 'monto')
    list_filter = ('fecha', 'vendedor')
    search_fields = ('vendedor__nombre',)
