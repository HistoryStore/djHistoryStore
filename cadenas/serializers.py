from rest_framework import serializers
from .models import Vendor, Place


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('id', 'name', 'image',)


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'image', 'latitude', 'longitude',)
