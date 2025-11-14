# Sistema de Login Implementado

## Descripción

Se ha implementado un sistema completo de autenticación de usuarios para el proyecto Django.

## Cambios Realizados

### 1. **Views (minicore/views.py)**

Se agregaron tres nuevas vistas de autenticación:

- `login_view`: Maneja el login de usuarios
- `registro_view`: Gestiona el registro de nuevos usuarios
- `logout_view`: Cierra la sesión del usuario

Además, se protegieron las vistas existentes con el decorador `@login_required`:

- `listar_vendedores()`
- `listar_ventas()`
- `crear_venta()`
- `editar_venta()`
- `eliminar_venta()`

### 2. **Formularios (minicore/forms.py)**

Se crearon dos nuevos formularios:

- `LoginForm`: Para el inicio de sesión (usuario y contraseña)
- `RegistroForm`: Para el registro de nuevos usuarios (usuario, email, contraseña, confirmar contraseña)

### 3. **Templates**

Se crearon dos nuevos templates:

- `login.html`: Página de inicio de sesión
- `registro.html`: Página de registro de nuevos usuarios

Se actualizó el template existente:

- `base.html`: Se agregó una barra de navegación mejorada con opciones de login/registro/logout
- `home.html`: Se personaliza el mensaje según si el usuario está autenticado o no

### 4. **URLs (comisiones/urls.py)**

Se agregaron tres nuevas rutas:

- `/login/`: Vista de login
- `/registro/`: Vista de registro
- `/logout/`: Vista de logout

## Características

✅ **Autenticación segura**: Usa el sistema de autenticación nativo de Django
✅ **Protección de vistas**: Las páginas de ventas y vendedores requieren login
✅ **Registro de usuarios**: Los nuevos usuarios pueden registrarse en el sistema
✅ **Validación de formularios**: Validaciones en cliente y servidor
✅ **Mensajes de retroalimentación**: Alertas visuales para el usuario
✅ **Interfaz responsive**: Diseño adaptable con Bootstrap 5

## Cómo Usar

### Crear un nuevo usuario:

1. Ir a `/registro/`
2. Completar el formulario con:
   - Usuario único
   - Email válido
   - Contraseña segura
3. Confirmar contraseña

### Iniciar Sesión:

1. Ir a `/login/`
2. Ingresar usuario y contraseña
3. Se redirige automáticamente a la página de inicio

### Cerrar Sesión:

- Hacer clic en el dropdown del usuario en la navbar
- Seleccionar "Cerrar sesión"

## Notas de Seguridad

- Las contraseñas se hashean automáticamente usando los validadores de Django
- Las contraseñas cumplen con los estándares de seguridad de Django:
  - Longitud mínima de 8 caracteres
  - No pueden ser contraseñas comunes
  - No pueden ser solo números
  - No pueden ser similares al nombre de usuario

## Próximas Mejoras Sugeridas

- [ ] Validación de email (enviar confirmación por correo)
- [ ] Recuperación de contraseña olvidada
- [ ] Autenticación de dos factores (2FA)
- [ ] Perfiles de usuario mejorados
- [ ] Registro de actividades (audit log)
