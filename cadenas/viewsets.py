__author__ = 'richpolis'
#To change this template use Tools | Templates.

from .models import Place
form .serializers import PlaceSerializer
from rest_framework import viewsets


class PlaceViewSet(viewsets.ModelViewSet):
	serializer_class = PlaceSerializer
	queryset = Place.objects.all()
