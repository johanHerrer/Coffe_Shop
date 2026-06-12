from django.shortcuts import render

def home(request):

    return render(
        request,
        'pages/home.html'
    )

def dashboard(request):

    return render(
        request,
        'dashboard/index.html'
    )