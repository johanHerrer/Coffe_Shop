from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Payment
from .serializers import PaymentSerializer


@api_view(['GET'])
def payments_api(request):
    payments = Payment.objects()
    serializer = PaymentSerializer(payments, many=True)
    return Response(serializer.data)
