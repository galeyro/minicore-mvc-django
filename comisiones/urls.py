"""
URL configuration for comisiones project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from minicore import views
from mozilla_django_oidc.views import OIDCAuthenticationCallbackView

urlpatterns = [
    path('admin/', admin.site.urls),
    # OIDC callback explícita
    path('oidc/callback/', OIDCAuthenticationCallbackView.as_view(), name='oidc_callback'),
    # Otras URLs de OIDC
    path('oidc/', include('mozilla_django_oidc.urls')),
    # Ruta de login personalizada
    path('oidc-login/', views.login_redirect, name='oidc_login'),
    path('logout/', views.logout_view, name='logout'),
    # Rutas principales
    path('', views.home, name='home'),
    path('vendedores/', views.listar_vendedores, name='listar_vendedores'),
    path('ventas/', views.listar_ventas, name='listar_ventas'),
    path('ventas/crear/', views.crear_venta, name='crear_venta'),
    path('ventas/editar/<int:pk>/', views.editar_venta, name='editar_venta'),
    path('ventas/eliminar/<int:pk>/', views.eliminar_venta, name='eliminar_venta'),
]
