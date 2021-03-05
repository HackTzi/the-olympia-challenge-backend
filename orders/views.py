"""Orders views."""

# Django REST Framework
from rest_framework import viewsets, permissions

# Models
from orders.models import Order

# Serializers
from orders.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = (permissions.IsAuthenticated,)
