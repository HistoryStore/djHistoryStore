from .models import Place
from .serializers import PlaceSerializer
from rest_framework import viewsets


class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
