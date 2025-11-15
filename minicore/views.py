from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from mozilla_django_oidc.views import OIDCAuthenticationRequestView
from .models import Vendedor, Venta, Reglas
from .forms import VentaForm

def login_redirect(request):
    """Redirige al login de Keycloak"""
    from mozilla_django_oidc.views import OIDCAuthenticationRequestView
    auth_view = OIDCAuthenticationRequestView()
    auth_view.request = request
    return auth_view.get(request)

def logout_view(request):
    """Cierra sesión en Django y Keycloak"""
    logout(request)
    return redirect('/')

def home(request):
    return render(request, 'home.html')

@login_required(login_url='oidc_login')
def listar_vendedores(request):
    vendedores = Vendedor.objects.all()
    return render(request, 'vendedor.html', {'vendedores': vendedores})

@login_required(login_url='oidc_login')
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

@login_required(login_url='oidc_login')
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

@login_required(login_url='oidc_login')
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

@login_required(login_url='oidc_login')
def eliminar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        messages.success(request, 'Venta eliminada exitosamente.')
        return redirect('listar_ventas')
    
    return render(request, 'venta_confirm_delete.html', {'venta': venta})