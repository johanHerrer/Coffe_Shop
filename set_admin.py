"""
Script para asignar rol de admin a un usuario
Ejecutar: python set_admin.py
"""

import os
import sys
import django

# Configurar Django
sys.path.insert(0, os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.users.models import User, Role

# Obtener email del usuario
email = input("Ingrese el email del usuario a hacer admin: ").strip()

# Buscar usuario
user = User.objects(email=email).first()

if not user:
    print(f"✗ Usuario con email '{email}' no encontrado")
    sys.exit(1)

# Obtener rol admin
admin_role = Role.objects(name='admin').first()

if not admin_role:
    print("✗ Rol 'admin' no existe. Ejecute init_roles.py primero")
    sys.exit(1)

# Asignar rol
user.role = admin_role
user.save()

print(f"✓ Usuario '{user.full_name}' ahora es administrador")
