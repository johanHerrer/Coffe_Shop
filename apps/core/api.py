from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.products.models import Product
from apps.orders.models import Order
from .serializers import DashboardSerializer


@api_view(['GET'])
def dashboard_api(request):
    products = Product.objects().count()
    orders = Order.objects().count()
    sales = sum(order.total for order in Order.objects())

    serializer = DashboardSerializer({
        'products': products,
        'orders': orders,
        'sales': sales,
    })

    return Response(serializer.data)
