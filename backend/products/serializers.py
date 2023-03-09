from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    new_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'new_discount'
        ]

    def get_new_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.discount()