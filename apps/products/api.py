from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product
from .serializers import ProductSerializer



@api_view(['GET'])
def products_api(request):

    products = Product.objects()

    serializer = ProductSerializer(
        products,
        many=True
    )

    return Response(
        serializer.data
    )