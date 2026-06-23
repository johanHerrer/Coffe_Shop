from rest_framework import serializers


class DashboardSerializer(serializers.Serializer):
    products = serializers.IntegerField()
    orders = serializers.IntegerField()
    sales = serializers.FloatField()
