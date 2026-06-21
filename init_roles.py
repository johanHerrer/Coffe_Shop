"""
Script para inicializar roles en la base de datos MongoDB
Ejecutar: python init_roles.py
"""

import os
import sys
import django

# Configurar Django
sys.path.insert(0, os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.users.models import Role

# Crear roles predeterminados
roles_data = [
    {
        'name': 'admin',
        'description': 'Administrador del sistema con acceso total'
    },
    {
        'name': 'user',
        'description': 'Usuario normal con acceso a compras'
    }
]

for role_data in roles_data:
    role = Role.objects(name=role_data['name']).first()
    
    if not role:
        role = Role(
            name=role_data['name'],
            description=role_data['description']
        )
        role.save()
        print(f"✓ Rol '{role_data['name']}' creado exitosamente")
    else:
        print(f"ℹ Rol '{role_data['name']}' ya existe")

print("\nRoles inicializados correctamente")
