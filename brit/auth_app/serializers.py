from rest_framework import serializers

from .models import Products

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    price = serializers.CharField(required=True)

    class Meta:
        model = Products
        fields = ("name", "price")