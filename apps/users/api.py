from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


@api_view(['GET'])
def users_api(request):
    users = User.objects()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
