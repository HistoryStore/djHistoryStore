from .models import List, Shopping
from .serializers import ListSerializer, ShoppingSerializer
from rest_framework import viewsets


class ListViewSet(viewsets.ModelViewSet):
    serializer_class = ListSerializer
    queryset = List.objects.all()


class ShoppingViewSet(viewsets.ModelViewSet):
    serializer_class = ShoppingSerializer
    queryset = Shopping.objects.all()
