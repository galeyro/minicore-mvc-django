from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from .models import Vendedor, Venta, Reglas
from .forms import VentaForm, LoginForm, RegistroForm

@require_http_methods(["GET", "POST"])
def login_view(request):
    """Vista de login de usuarios"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            contraseña = form.cleaned_data['contraseña']
            user = authenticate(request, username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido {user.username}!')
                return redirect('home')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

@require_http_methods(["GET", "POST"])
def registro_view(request):
    """Vista de registro de nuevos usuarios"""
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            email = form.cleaned_data['email']
            contraseña = form.cleaned_data['contraseña']
            confirmar_contraseña = form.cleaned_data['confirmar_contraseña']
            
            if contraseña != confirmar_contraseña:
                messages.error(request, 'Las contraseñas no coinciden.')
                return render(request, 'registro.html', {'form': form})
            
            if User.objects.filter(username=usuario).exists():
                messages.error(request, 'El usuario ya existe.')
                return render(request, 'registro.html', {'form': form})
            
            if User.objects.filter(email=email).exists():
                messages.error(request, 'El email ya está registrado.')
                return render(request, 'registro.html', {'form': form})
            
            user = User.objects.create_user(username=usuario, email=email, password=contraseña)
            user.save()
            messages.success(request, 'Registro exitoso. Por favor, inicia sesión.')
            return redirect('login')
    else:
        form = RegistroForm()
    
    return render(request, 'registro.html', {'form': form})

@require_http_methods(["POST"])
def logout_view(request):
    """Vista de logout de usuarios"""
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente.')
    return redirect('home')

def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def listar_vendedores(request):
    vendedores = Vendedor.objects.all()
    return render(request, 'vendedor.html', {'vendedores': vendedores})

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def eliminar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        messages.success(request, 'Venta eliminada exitosamente.')
        return redirect('listar_ventas')
    
    return render(request, 'venta_confirm_delete.html', {'venta': venta})