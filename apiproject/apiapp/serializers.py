from rest_framework import serializers
from .models import Category, Product, Order, CustomUser
from django.contrib.auth import get_user_model

# Category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

# Product serializer with nested category details
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True) 
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category', 'category_id', 'image', 'image_url']
        read_only_fields = ['image']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None

# For upload-only image endpoint
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'image']

# Custom user serializer (register)
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password']
    
    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data.get('username'),
            email=validated_data.get('email')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

# Order serializer
class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, source='product')

    class Meta:
        model = Order
        fields = ['id', 'user', 'product', 'product_id', 'quantity', 'total_price', 'status', 'created_at', 'updated_at']
        read_only_fields = ['total_price', 'status', 'created_at', 'updated_at']
