from rest_framework import serializers
from .models import Vendor, Place


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('id', 'name', 'image',)


class PlaceSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer(read_only=True)
    vendor_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Vendor.objects.all(), source='vendor')

    class Meta:
        model = Place
        fields = ('id', 'name', 'vendor', 'vendor_id', 'latitude', 'longitude',)
