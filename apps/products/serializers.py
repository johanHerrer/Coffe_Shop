from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.Serializer):

    id = serializers.CharField()

    name = serializers.CharField()

    description = serializers.CharField(allow_blank=True, required=False, allow_null=True)

    price = serializers.FloatField()

    stock = serializers.IntegerField()

    image = serializers.CharField(allow_blank=True, required=False, allow_null=True)

    available = serializers.BooleanField()

    featured = serializers.BooleanField()

    is_on_demand = serializers.BooleanField()
