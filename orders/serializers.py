"""Serializers orders."""

# Django REST Framework
from rest_framework import serializers

# Models
from orders.models import Order, ProductOrder


class ProductOrderSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = ProductOrder
        fields = ('product', 'quantity', 'author')
        read_only_fields = ('author', 'created_at', 'modified_at')


class OrderSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    products = ProductOrderSerializer(many=True)

    class Meta:
        model = Order
        fields = ('customer', 'shipping_address', 'products', 'coupon', 'products_price',
                  'shipping_price', 'tax_price', 'author', 'created_at', 'modified_at')
        read_only_fields = ('author', 'created_at', 'modified_at')
