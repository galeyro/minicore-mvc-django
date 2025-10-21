from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Vendedor, Venta, Reglas
from .forms import VentaForm

def home(request):
    return render(request, 'home.html')

def listar_vendedores(request):
    vendedores = Vendedor.objects.all()
    return render(request, 'vendedor.html', {'vendedores': vendedores})

def listar_ventas(request):
    ventas = Venta.objects.select_related('vendedor').all()
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    if fecha_inicio and fecha_fin:
        ventas = ventas.filter(fecha__range=[fecha_inicio, fecha_fin])
    
    ventas_con_comision = []
    for venta in ventas:
        regla = Reglas.objects.filter(monto_min__lte=venta.monto, monto_max__gte=venta.monto).first()
        comision = 0
        if regla:
            comision = venta.monto * (regla.porcentaje / 100)
        ventas_con_comision.append({
            'venta' : venta,
            'comision': round(comision, 2),
        })

    context = {
        'ventas_con_comision': ventas_con_comision,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
    }
    return render(request, 'ventas.html', context)

def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Venta creada exitosamente.')
            return redirect('listar_ventas')
    else:
        form = VentaForm()
    
    return render(request, 'venta_form.html', {'form': form, 'accion': 'Crear'})

def editar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Venta actualizada exitosamente.')
            return redirect('listar_ventas')
    else:
        form = VentaForm(instance=venta)
    
    return render(request, 'venta_form.html', {'form': form, 'accion': 'Editar'})

def eliminar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        messages.success(request, 'Venta eliminada exitosamente.')
        return redirect('listar_ventas')
    
    return render(request, 'venta_confirm_delete.html', {'venta': venta})