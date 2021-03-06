"""Customer Serializer"""

# Django REST framework
from rest_framework import serializers

# Models
from django.contrib.auth.models import User
from customers.models import Customer, ShippingAddress, Currency, Country, Notification


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'user', 'picture', 'work_area', 'preferences', 'language',
                  'phone_number', 'currency', 'points', 'created_at', 'modified_at', 'author',)
        read_only_fields = ('points', 'created_at', 'modified_at')


class ShippingAddressSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = ShippingAddress
        fields = ('customer', 'country', 'address', 'city', 'state', 'zip_code',
                  'created_at', 'modified_at', 'author',)
        read_only_fields = ('author', 'created_at', 'modified_at')


class CurrencySerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Currency
        fields = '__all__'
        read_only_fields = ('author', 'created_at', 'modified_at')


class CountrySerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Country
        fields = ('id', 'name', 'tax_rate', 'created_at', 'modified_at', 'author')
        read_only_fields = ('author', 'created_at', 'modified_at')


class NotificationSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Notification
        fields = ('id', 'customer', 'content', 'type', 'created_at', 'modified_at', 'author')
        read_only_fields = ('author', 'created_at', 'modified_at')
