from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .services import AuthService
from .models import User

def register_view(request):

    form = RegisterForm()

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            AuthService.create_user(
                form.cleaned_data
            )

            return redirect('login')

    return render(
        request,
        'auth/register.html',
        {
            'form': form
        }
    )

def login_view(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects(
                email=email
            ).first()

            if user and AuthService.verify_password(
                password,
                user.password
            ):

                request.session['user_id'] = str(user.id)
                request.session['user_name'] = user.full_name

                return redirect('home')

    return render(
        request,
        'auth/login.html',
        {
            'form': form
        }
    )

def logout_view(request):

    request.session.flush()

    return redirect('home')