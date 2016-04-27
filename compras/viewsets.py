from .models import List
from .serializers import ListSerializer
from rest_framework import viewsets, filters


class ListViewSet(viewsets.ModelViewSet):
    serializer_class = ListSerializer
    queryset = List.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('user__email',)
    search_fields = ('user__email',)


# class ShoppingViewSet(viewsets.ModelViewSet):
#     serializer_class = ShoppingSerializer
#     queryset = Shopping.objects.all()
#     filter_backends = (filters.DjangoFilterBackend,)
#     filter_fields = ('list__user__email', 'list__place__name', 'product__name', 'product__key')
#     search_fields = ('list__place__name', 'product__name', 'product__key',)
#     ordering_fields = ('list', 'product')
