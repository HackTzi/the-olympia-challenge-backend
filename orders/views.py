"""Orders views."""

# Django REST Framework
from rest_framework import viewsets, permissions, exceptions
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from orders.models import Order, Payment

# Serializers
from orders.serializers import OrderSerializer, OrderTrackingSerializer, PaymentSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # permission_classes = (permissions.IsAuthenticated,)

    @action(detail=True, methods=['post'])
    def order_tracking(self, request, pk=None):
        if request.method == 'POST':
            request.data['order'] = pk

            serializer = OrderTrackingSerializer(request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)

            serializer.create(serializer.validated_data)
            return Response(serializer.data)

    @action(detail=True, methods=['post', 'get'])
    def payment(self, request, pk=None):
        if request.method == 'POST':
            pass
        elif request.method == 'GET':
            try:
                payment = Payment.objects.get(pk=pk)
            except Payment.DoesNotExist:
                raise exceptions.NotFound(f'')

            serializer = PaymentSerializer(payment)

            return Response(serializer.data)
