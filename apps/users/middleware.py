from django.shortcuts import redirect
from apps.users.models import User

class AuthRequiredMiddleware:

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):
        protected_routes = [
            '/dashboard/'
        ]

        if request.path.startswith('/dashboard/'):
            user_id = request.session.get(
                'user_id'
            )

            if not user_id:
                return redirect('login')

            user = User.objects(
                id=user_id
            ).first()

            if not user.role or user.role.name != "admin":
                return redirect('home')

        response = self.get_response(request)
        return response