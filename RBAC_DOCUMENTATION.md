# Sistema de Control de Acceso por Roles

## Resumen de Cambios

Se ha implementado un sistema de control de acceso basado en roles (RBAC) en el proyecto. Esto permite que solo los administradores puedan crear y eliminar productos, mientras que los usuarios normales solo pueden ver productos y hacer compras.

## Características

### 1. Roles Disponibles
- **admin**: Acceso total al sistema, puede crear/editar/eliminar productos
- **user**: Usuario normal, solo puede ver productos y realizar compras

### 2. Restricciones de Acceso

#### Vistas Protegidas
- `create_product`: Solo administradores pueden crear productos
- `delete_product`: Solo administradores pueden eliminar productos
- `dashboard_orders`: Solo administradores pueden ver el dashboard de órdenes

#### Interfaz de Usuario
- El botón "Nuevo Producto" solo aparece para administradores
- El botón "Eliminar" en tarjetas de productos solo aparece para administradores
- El enlace "Dashboard" en navbar solo aparece para administradores

## Instalación y Configuración

### 1. Inicializar Roles
Ejecutar el script de inicialización:
```bash
python init_roles.py
```
Esto crea los roles "admin" y "user" en la base de datos.

### 2. Asignar Rol de Administrador
Para convertir un usuario existente en administrador:
```bash
python set_admin.py
```
Ingrese el email del usuario cuando se solicite.

### 3. Crear Usuario Administrador
Registre un usuario normalmente, luego ejecute:
```bash
python set_admin.py
```

## Archivos Modificados

### Nuevos Archivos
- `apps/users/decorators.py`: Contiene el decorador `@admin_required`
- `init_roles.py`: Script para inicializar roles en la BD
- `set_admin.py`: Script para asignar rol admin a usuarios

### Archivos Modificados
- `apps/users/views.py`: Actualizado para guardar `user_role` en sesión
- `apps/users/middleware.py`: Agregado decorador admin_required
- `apps/products/views.py`: Protegidas vistas con decorador `@admin_required`
- `apps/orders/views.py`: Protegida vista dashboard_orders
- `templates/products/list.html`: Botón "Nuevo Producto" condicional
- `templates/products/components/product_card.html`: Botón "Eliminar" condicional
- `templates/components/navbar.html`: Enlace "Dashboard" condicional

## Cómo Funciona

### Session Storage
Cuando un usuario inicia sesión, se almacena en la sesión:
```python
request.session['user_id'] = str(user.id)
request.session['user_name'] = user.full_name
request.session['user_role'] = user.role.name if user.role else 'user'
```

### Decorador admin_required
Todas las vistas de admin utilizan el decorador:
```python
@admin_required
def create_product(request):
    # Solo los admins pueden ver esta vista
    ...
```

Si un usuario no administrador intenta acceder, es redirigido a la página de productos.

### Validación en Templates
Las opciones de admin se muestran condicionalmente:
```html
{% if request.session.user_role == 'admin' %}
    <!-- Contenido solo para admins -->
{% endif %}
```

## Flujos de Acceso

### Usuario Normal
1. Registra cuenta
2. Inicia sesión → rol = "user"
3. Puede ver productos
4. Puede agregar a carrito
5. Puede comprar
6. NO puede crear/editar/eliminar productos
7. NO puede acceder a dashboard

### Administrador
1. Se crea usuario normalmente
2. Se ejecuta `set_admin.py` para asignar rol
3. Inicia sesión → rol = "admin"
4. Puede ver dashboard
5. Puede crear nuevos productos
6. Puede eliminar productos
7. Puede gestionar órdenes

## Validación de Seguridad

### Backend
- Todas las vistas protegidas validan `user_role` en sesión
- Si `user_role != 'admin'`, redirige a productos
- Si no está logueado, redirige a login

### Frontend
- Los botones solo aparecen si `request.session.user_role == 'admin'`
- Esto mejora la UX pero NO es suficiente por sí solo
- La seguridad real está en el backend

## Próximas Mejoras (Opcionales)

1. Agregar más roles (moderador, vendedor)
2. Implementar permisos granulares
3. Agregar auditoría de acciones de admin
4. Dashboard de estadísticas
5. Gestión de usuarios desde admin

## Testing

Para probar el sistema:

### Test 1: Usuario Normal
```
1. Registrar nuevo usuario
2. Iniciar sesión
3. Ir a /products/create → debe redirigir a /products
4. No debe ver botón "Nuevo Producto"
```

### Test 2: Usuario Admin
```
1. Registrar usuario
2. Ejecutar: python set_admin.py
3. Iniciar sesión
4. Ir a /products/create → debe mostrar formulario
5. Debe ver botón "Nuevo Producto"
6. Debe ver botón "Eliminar" en cada producto
```
