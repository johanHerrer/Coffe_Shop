from django.shortcuts import redirect

class AuthRequiredMiddleware:

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):

        protected_routes = [
            '/dashboard/',
        ]

        if request.path in protected_routes:

            if not request.session.get('user_id'):

                return redirect('login')

        response = self.get_response(request)

        return response