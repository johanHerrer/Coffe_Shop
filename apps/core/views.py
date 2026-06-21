from django.shortcuts import render
from apps.products.models import Product
from apps.orders.models import Order


def home(request):

    return render(
        request,
        'pages/home.html'
    )

def dashboard(request):


    products = Product.objects.count()


    orders = Order.objects.count()


    sales = sum(

        order.total

        for order in Order.objects

    )


    return render(

        request,

        "dashboard/index.html",

        {

        "products":products,

        "orders":orders,

        "sales":sales

        }

    )