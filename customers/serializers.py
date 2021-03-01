"""Customer Serializer"""

# Django REST framework
from rest_framework import serializers

# Models
from django.contrib.auth.models import User
from customers.models import Customer, ShippingAddress


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True, read_only=False)
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Customer
        fields = ('user', 'picture', 'work_area', 'preferences', 'language',
                  'phone_number', 'currency', 'points', 'created_at', 'modified_at', 'author',)
        read_only_fields = ('points', 'author', 'created_at', 'modified_at')


class ShippingAddressSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = ShippingAddress
        fields = ('customer', 'country', 'address', 'city', 'state', 'zip_code',
                  'created_at', 'modified_at', 'author',)
        read_only_fields = ('author', 'created_at', 'modified_at')
