from .models import Vendor, Place
from .serializers import VendorSerializer, PlaceSerializer
from rest_framework import viewsets


class VendorViewSet(viewsets.ModelViewSet):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()


class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()