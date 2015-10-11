from .models import List, Shopping
from .serializers import ListSerializer, ShoppingSerializer
from rest_framework import viewsets, filters


class ListViewSet(viewsets.ModelViewSet):
    serializer_class = ListSerializer
    queryset = List.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('user__email', 'place__name','vendor__name')
    search_fields = ('place__name', 'vendor__name', 'user__email',)


class ShoppingViewSet(viewsets.ModelViewSet):
    serializer_class = ShoppingSerializer
    queryset = Shopping.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('list__user__email', 'list__place__name','list__vendor__name', 'product__name', 'product__key')
    search_fields = ('list__place__name','list__vendor__name', 'product__name', 'product__key',)
    ordering_fields = ('list', 'product')
