from .models import Category, Product, Comment
from django.contrib.auth.models import User
from .serializers import CategorySerializer, ProductSerializer, CommentSerializer, UserSerializer
from rest_framework import viewsets, filters


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('user__email', 'product__name','product__category__name')
    search_fields = ('user__email', 'product__name','product__category__name',)
