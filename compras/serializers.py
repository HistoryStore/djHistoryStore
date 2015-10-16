from rest_framework import serializers
from .models import List, Shopping
from productos.serializers import ProductSerializer, UserSerializer
from productos.models import Category, Product, User
from cadenas.serializers import PlaceSerializer, VendorSerializer
from cadenas.models import Place, Vendor


class ListSerializer(serializers.ModelSerializer):
    place = PlaceSerializer(read_only=True)
    place_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Place.objects.all(), source='place')
    # vendor = VendorSerializer(read_only=True)
    # vendor_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Vendor.objects.all(), source='vendor')
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), source='user')

    class Meta:
        model = List
        fields = ('id', 'date_shopping', 'place', 'place_id', 'status', 'user','user_id', 'total',)
        read_only_fields = ('date_shopping',)


class ShoppingSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Product.objects.all(), source='product')
    list = ListSerializer(read_only=True)
    list_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=List.objects.all(), source='list')

    class Meta:
        model = Shopping
        fields = ('id', 'product','product_id', 'list','list_id',  'price', 'quantity', 'total',)
