from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.Serializer):

    id = serializers.CharField()

    name = serializers.CharField()

    description = serializers.CharField()

    price = serializers.FloatField()

    stock = serializers.IntegerField()

    image = serializers.CharField()
