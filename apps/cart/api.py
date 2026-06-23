from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cart
from .serializers import CartSerializer


@api_view(['GET'])
def cart_api(request):
    carts = Cart.objects()
    serializer = CartSerializer(carts, many=True)
    return Response(serializer.data)
