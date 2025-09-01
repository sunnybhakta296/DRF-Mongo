# serializers.py
# Django REST Framework serializers for User, Product, and Order models.

from rest_framework import serializers
from .models import User, Product, Order

# UserSerializer: Handles serialization and deserialization of User objects.
class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)  # User ID (read-only)
    username = serializers.CharField()          # Username
    email = serializers.EmailField()            # Email address
    password = serializers.CharField(write_only=True)  # Password (write-only)

    def create(self, validated_data):
        """
        Create and return a new User instance, given the validated data.
        """
        user = User(**validated_data)
        user.save()
        return user

    def update(self, instance, validated_data):
        """
        Update and return an existing User instance, given the validated data.
        """
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

# ProductSerializer: Handles serialization and deserialization of Product objects.
class ProductSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)      # Product ID (read-only)
    name = serializers.CharField()                  # Product name
    description = serializers.CharField(allow_blank=True)  # Product description (optional)
    price = serializers.FloatField()                # Product price

    def create(self, validated_data):
        """
        Create and return a new Product instance, given the validated data.
        """
        product = Product(**validated_data)
        product.save()
        return product

    def update(self, instance, validated_data):
        """
        Update and return an existing Product instance, given the validated data.
        """
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

# OrderSerializer: Handles serialization and deserialization of Order objects.
class OrderSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)      # Order ID (read-only)
    user = serializers.CharField()                  # User ID (references User)
    products = serializers.ListField(child=serializers.CharField())  # List of Product IDs
    created_at = serializers.DateTimeField(read_only=True)           # Order creation timestamp (read-only)

    def to_representation(self, instance):
        """
        Customize the representation of the Order instance.
        Expands user and products fields to nested objects.
        """
        rep = super().to_representation(instance)
        rep['user'] = UserSerializer(instance.user).data
        rep['products'] = ProductSerializer(instance.products, many=True).data
        return rep

    def create(self, validated_data):
        """
        Create and return a new Order instance, given the validated data.
        Resolves user and products from their IDs.
        """
        user = User.objects(id=validated_data['user']).first()
        products = [Product.objects(id=pid).first() for pid in validated_data.get('products', [])]
        order = Order(user=user, products=products)
        order.save()
        return order

    def update(self, instance, validated_data):
        """
        Update and return an existing Order instance, given the validated data.
        Resolves user and products from their IDs if provided.
        """
        if 'user' in validated_data:
            instance.user = User.objects(id=validated_data['user']).first()
        if 'products' in validated_data:
            instance.products = [Product.objects(id=pid).first() for pid in validated_data['products']]
        instance.save()
        return instance

