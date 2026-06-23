from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import InventoryMovement
from .serializers import InventoryMovementSerializer


@api_view(['GET'])
def inventory_api(request):
    movements = InventoryMovement.objects()
    serializer = InventoryMovementSerializer(movements, many=True)
    return Response(serializer.data)
