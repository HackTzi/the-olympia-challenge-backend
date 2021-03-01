"""Serializers orders."""

# Django REST Framework
from django.db.models import fields
from rest_framework import serializers

# Models
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('author', 'created_at', 'modified_at')
