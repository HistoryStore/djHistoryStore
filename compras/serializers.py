from rest_framework import serializers
from .models import List
from productos.serializers import *
from vendor.serializers import *

class DefaultListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'date_shopping', 'status']

class ListSerializer(serializers.ModelSerializer):
    user = DefaultUserSerializer(read_only=True)
    products = DefaultProductSerializer(many=True, required=False)
    place = DefaultPlaceSerializer(many=False, read_only=True)

    user_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), source='user')
    place_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Place.objects.all(), source='place')

    class Meta:
        model = List
        fields = ('id', 'date_shopping', 'status', 'user','user_id', 'place', 'place_id', 'products', )
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
