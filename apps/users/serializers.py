from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.CharField()
    full_name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField(allow_blank=True, required=False, allow_null=True)
    role = serializers.CharField(source='role.name', allow_blank=True, required=False, allow_null=True)
    is_active = serializers.BooleanField()
