from rest_framework import serializers


class InventoryMovementSerializer(serializers.Serializer):
    id = serializers.CharField()
    product_id = serializers.CharField(source='product.id')
    movement_type = serializers.CharField()
    quantity = serializers.IntegerField()
