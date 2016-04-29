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

    category = DefaultCategorySerializer(read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Category.objects.all(), source='category')

    class Meta:
        model = Product
        fields = ('id', 'code', 'name', 'image', 'category', 'category_id', 'type_uom', 'conversion')

class CommentSerializer(serializers.ModelSerializer):
    user = DefaultUserSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    user_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), source='user')
    product_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Product.objects.all(), source='product')

    class Meta:
        model = Comment
        fields = ('id', 'user', 'user_id', 'product', 'product_id', 'comment', 'qualification', 'created_at')
        read_only_fields = ('created_at',)
