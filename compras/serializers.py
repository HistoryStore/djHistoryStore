from rest_framework import serializers
from .models import List, Shopping


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ('id', 'date_shopping', 'total', 'place', 'vendor', 'status', 'user',)


class ShoppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopping
        fields = ('id', 'product', 'list','type_uom','price', 'conversion', 'quantity','total',)
