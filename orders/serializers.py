"""Serializers orders."""

# Django REST Framework
from rest_framework import serializers
from rest_framework.response import Response

# Models
from orders.models import Order, ProductOrder, OrderTracking


class ProductOrderSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = ProductOrder
        fields = ('product', 'quantity', 'author')
        read_only_fields = ('author', 'created_at', 'modified_at')


class OrderTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTracking
        fields = ('order', 'type', 'observations', 'created_at', 'modified_at')
        read_only_fields = ('author', 'created_at', 'modified_at')


class OrderSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    products = ProductOrderSerializer(many=True)
    tracking = serializers.SerializerMethodField

    class Meta:
        model = Order
        fields = ('customer', 'shipping_address', 'products', 'coupon', 'products_price',
                  'shipping_price', 'tax_price', 'tracking', 'author', 'created_at', 'modified_at')
        read_only_fields = ('author', 'created_at', 'modified_at')

    def get_tracking(self, order):
        order_tracking = OrderTracking(order=order)

        serializer = OrderTrackingSerializer(order_tracking)

        return Response(serializer.data)
