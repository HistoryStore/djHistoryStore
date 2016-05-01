from rest_framework import serializers
from .models import Category, Product, Comment
from django.contrib.auth.models import User

#----------Default serializers with only attributes----------#
class DefaultUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email',)

class DefaultCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)

class DefaultProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'code', 'name', 'image', 'type_uom', 'conversion']

# ----------Serializers with attributes and relations----------#
class CategorySerializer(serializers.ModelSerializer):

    products = DefaultProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'products']

class ProductSerializer(serializers.ModelSerializer):

    category = DefaultCategorySerializer(many=False)

    class Meta:
        model = Product
        fields = ('id', 'code', 'name', 'image', 'category', 'type_uom', 'conversion')
        read_only_fields = ['image']

class CommentSerializer(serializers.ModelSerializer):
    user = DefaultUserSerializer(many=False)
    product = ProductSerializer(many=False)

    class Meta:
        model = Comment
        fields = ('id', 'user', 'product', 'comment', 'qualification', 'created_at')
        read_only_fields = ('created_at',)
