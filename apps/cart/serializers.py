from rest_framework import serializers


class CartItemSerializer(serializers.Serializer):
    product_id = serializers.CharField(source='product.id')
    product_name = serializers.CharField(source='product.name')
    quantity = serializers.IntegerField()
    price = serializers.FloatField(source='product.price')
    subtotal = serializers.FloatField(source='subtotal')


class CartSerializer(serializers.Serializer):
    id = serializers.CharField()
    user_id = serializers.CharField()
    total = serializers.FloatField()
    items = CartItemSerializer(many=True)
