from rest_framework import serializers


class OrderItemSerializer(serializers.Serializer):
    product_id = serializers.CharField(source='product.id')
    product_name = serializers.CharField(source='product.name')
    quantity = serializers.IntegerField()
    price = serializers.FloatField()
    subtotal = serializers.FloatField(source='subtotal')


class OrderSerializer(serializers.Serializer):

    id = serializers.CharField()

    user_id = serializers.CharField()

    total = serializers.FloatField()

    status = serializers.CharField()

    address = serializers.CharField(allow_blank=True, required=False, allow_null=True)

    items = OrderItemSerializer(many=True)