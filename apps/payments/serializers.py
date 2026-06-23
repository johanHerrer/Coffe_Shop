from rest_framework import serializers


class PaymentSerializer(serializers.Serializer):
    id = serializers.CharField()
    amount = serializers.FloatField()
    currency = serializers.CharField()
    status = serializers.CharField()
    method = serializers.CharField(allow_blank=True, required=False, allow_null=True)
