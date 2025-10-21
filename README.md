# 💼 Sistema de Comisiones - Django

Sistema web desarrollado en Django para la gestión de ventas y cálculo automático de comisiones basado en reglas de negocio configurables.

## 📋 Características

- ✅ **CRUD completo de Ventas**: Crear, leer, actualizar y eliminar ventas
- 📊 **Cálculo automático de comisiones**: Basado en rangos de monto configurables
- 📅 **Filtrado por fechas**: Consulta ventas en rangos de fechas específicos
- 👥 **Gestión de vendedores**: Lista de vendedores registrados
- ⚙️ **Reglas personalizables**: Configuración de rangos y porcentajes desde el admin
- 🎨 **Interfaz simple y responsiva**: Diseñada con Bootstrap 5

## 🗂️ Estructura del Proyecto

```
minicore-mvc-django/
├── comisiones/           # Configuración del proyecto Django
│   ├── settings.py       # Configuración general
│   ├── urls.py          # Rutas principales
│   └── wsgi.py          # Entrada WSGI
├── minicore/            # Aplicación principal
│   ├── models.py        # Modelos: Vendedor, Venta, Reglas
│   ├── views.py         # Vistas del CRUD
│   ├── forms.py         # Formularios
│   ├── admin.py         # Configuración del admin
│   └── templates/       # Plantillas HTML
│       ├── base.html
│       ├── home.html
│       ├── vendedor.html
│       ├── ventas.html
│       ├── venta_form.html
│       └── venta_confirm_delete.html
├── db.sqlite3           # Base de datos SQLite
└── manage.py            # Comando de gestión Django
```

## 🚀 Instalación y Configuración

### Requisitos previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/galeyro/minicore-mvc-django.git
   cd minicore-mvc-django
   ```

2. **Crear y activar entorno virtual** (recomendado)

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar dependencias**

   ```bash
   pip install django
   ```

4. **Aplicar migraciones**

   ```bash
   python manage.py migrate
   ```

5. **Crear superusuario** (para acceder al admin)

   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar el servidor**

   ```bash
   python manage.py runserver
   ```

7. **Acceder a la aplicación**
   - Aplicación principal: http://127.0.0.1:8000/
   - Panel de administración: http://127.0.0.1:8000/admin/

## 📊 Modelos de Datos

### Vendedor

- `nombre`: Nombre del vendedor

### Reglas

- `nombre`: Nombre descriptivo de la regla
- `monto_min`: Monto mínimo del rango
- `monto_max`: Monto máximo del rango
- `porcentaje`: Porcentaje de comisión a aplicar

### Venta

- `vendedor`: Relación con el vendedor (ForeignKey)
- `fecha`: Fecha de la venta
- `monto`: Monto total de la venta

## 🔧 Uso del Sistema

### Gestionar Reglas de Comisión

Las reglas se configuran desde el panel de administración (`/admin/`):

1. Acceder con el superusuario
2. Ir a "Reglas"
3. Crear rangos de montos con sus porcentajes

**Ejemplo:**

- Bronce: $0 - $1000 → 5% comisión
- Plata: $1001 - $5000 → 10% comisión
- Oro: $5001 - $999999 → 15% comisión

### Gestionar Vendedores

Los vendedores también se gestionan desde el admin:

1. Ir a "Vendedores"
2. Agregar vendedores con su nombre

### Gestionar Ventas

Las ventas se gestionan desde la interfaz web:

1. **Crear venta**: Botón "Nueva Venta" o desde el menú
2. **Listar ventas**: Ver todas las ventas con comisiones calculadas
3. **Filtrar por fechas**: Usar los campos "Desde" y "Hasta"
4. **Editar venta**: Botón "Editar" en cada fila
5. **Eliminar venta**: Botón "Eliminar" con confirmación

## 🌐 Rutas Disponibles

| Ruta                     | Descripción                 |
| ------------------------ | --------------------------- |
| `/`                      | Página de inicio            |
| `/vendedores/`           | Lista de vendedores         |
| `/ventas/`               | Lista de ventas con filtros |
| `/ventas/crear/`         | Crear nueva venta           |
| `/ventas/editar/<id>/`   | Editar venta existente      |
| `/ventas/eliminar/<id>/` | Eliminar venta              |
| `/admin/`                | Panel de administración     |

## 🎯 Cómo Funciona el Cálculo de Comisiones

1. El sistema busca la regla que coincida con el monto de la venta
2. Aplica el porcentaje definido en esa regla
3. Muestra el resultado en la columna "Comisión"

**Ejemplo:**

- Venta de $3,500
- Regla aplicable: Plata ($1001 - $5000, 10%)
- Comisión calculada: $350

## 🛠️ Tecnologías Utilizadas

- **Django 5.2.3**: Framework web de Python
- **SQLite**: Base de datos (incluida por defecto)
- **Bootstrap 5.3.3**: Framework CSS para diseño responsivo
- **Python 3.x**: Lenguaje de programación

## 📦 Para Deployment

### Preparar para producción:

1. **Actualizar `settings.py`:**

   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['tu-dominio.com']
   SECRET_KEY = 'tu-clave-secreta-segura'
   ```

2. **Configurar base de datos de producción** (PostgreSQL, MySQL, etc.)

3. **Recolectar archivos estáticos:**

   ```bash
   python manage.py collectstatic
   ```

4. **Usar servidor WSGI** (Gunicorn, uWSGI)
   ```bash
   pip install gunicorn
   gunicorn comisiones.wsgi:application
   ```

## 📝 Notas

- Este proyecto está basado en un tutorial de filtrado por fechas y comisiones en Django
- La configuración actual usa SQLite, apropiada para desarrollo y pruebas
- Para producción se recomienda PostgreSQL o MySQL
- Las reglas y vendedores se gestionan exclusivamente desde el admin

## 👤 Autor

Adaptado por **galeyro**  
Basado en el proyecto original de Martín Lomas

## 📄 Licencia

Este proyecto es de código abierto y está disponible para fines educativos.

---

¿Necesitas ayuda? Revisa la [documentación oficial de Django](https://docs.djangoproject.com/) o abre un issue en el repositorio.
