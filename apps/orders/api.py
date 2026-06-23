from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer


@api_view(['GET'])
def orders_api(request):

    orders = Order.objects()

    serializer = OrderSerializer(
        orders,
        many=True
    )

    return Response(
        serializer.data
    )