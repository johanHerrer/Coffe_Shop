from django.shortcuts import redirect
from functools import wraps


def admin_required(view_func):
    """Decorador para requerir que el usuario sea administrador."""
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        user_id = request.session.get('user_id')
        user_role = request.session.get('user_role')
        
        if not user_id:
            return redirect('login')
        
        if user_role != 'admin':
            return redirect('products')
        
        return view_func(request, *args, **kwargs)
    return wrapped_view
