import re

with open(r'c:\Users\herre\Desktop\WorkSpace\coffee_shop\apps\orders\views.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Reemplazar dashboard_orders para agregar decorador
content = content.replace(
    'def dashboard_orders(request):',
    '@admin_required\ndef dashboard_orders(request):'
)

with open(r'c:\Users\herre\Desktop\WorkSpace\coffee_shop\apps\orders\views.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated dashboard_orders with @admin_required decorator')
