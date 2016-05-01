from rest_framework import serializers
from .models import List
from productos.serializers import *
from vendor.serializers import *

class DefaultListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'date_shopping', 'status']

class ListSerializer(serializers.ModelSerializer):
    user = DefaultUserSerializer(many=False)
    products = DefaultProductSerializer(many=True, required=False)
    place = PlaceSerializer(many=False)


    class Meta:
        model = List
        fields = ('id', 'date_shopping', 'status', 'user', 'place', 'products', )
        read_only_fields = ('date_shopping',)


# class ShoppingSerializer(serializers.ModelSerializer):
#     product = ProductSerializer(read_only=True)
#     product_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Product.objects.all(), source='product')
#     list = ListSerializer(read_only=True)
#     list_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=List.objects.all(), source='list')
#
#     class Meta:
#         model = Shopping
#         fields = ('id', 'product','product_id', 'list','list_id',  'price', 'quantity', 'total',)
