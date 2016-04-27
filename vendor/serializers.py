from rest_framework import serializers
from productos.serializers import DefaultCategorySerializer
from .models import *

#----------Default serializers with only attributes----------#
class DefaultVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name', 'image']

class DefaultPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'address', 'latitude', 'longitude']

# ----------Serializers with attributes and relations----------#
class VendorSerializer(serializers.ModelSerializer):
    places = DefaultPlaceSerializer(many=True, read_only=True)
    categories = DefaultCategorySerializer(many=True)

    class Meta:
        model = Vendor
        fields = ['id', 'name', 'image', 'places', 'categories']

class PlaceSerializer(serializers.ModelSerializer):
    vendor = DefaultVendorSerializer(many=False, read_only=True)

    vendor_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Vendor.objects.all(), source='vendor')

    class Meta:
        model = Place
        fields = ['id', 'address', 'latitude', 'longitude', 'vendor', 'vendor_id']