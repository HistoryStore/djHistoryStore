from rest_framework import serializers
from .models import Category, Product, Comment
from django.contrib.auth.models import User
from compras.models import List


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image',)


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Category.objects.all(),
                                                     source='category')
    list_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=List.objects.all(),
                                                 source='list')

    class Meta:
        model = Product
        fields = (
        'id', 'key', 'name', 'category', 'category_id', 'type_uom', 'conversion', 'price', 'quantity', 'list_id')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',)


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), source='user')
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Product.objects.all(), source='product')

    class Meta:
        model = Comment
        fields = ('id', 'user', 'user_id', 'product', 'product_id', 'comment', 'qualification', 'created_at')
        read_only_fields = ('created_at',)
