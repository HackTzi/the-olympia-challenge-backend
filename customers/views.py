"""Customer views"""

# Django REST Framework
from rest_framework import viewsets, mixins, exceptions
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from customers.models import Customer, ShippingAddress

# Serializers
from customers.serializers import CustomerSerializer, ShippingAddressSerializer


class CustomerViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(methods=['post'], detail=True)
    def points(self, request):
        customer = self.get_object()
        points = request.data.get('points', None)

        if points is None:
            raise exceptions.NotAcceptable(detail={'points': 'this field is required.'})

        customer.points += int(points)

        serializer = self.get_serializer()
        serializer(self.get_object())

        return Response(serializer.data)


class ShippingAddressViewSet(viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    http_method_names = [u'get', u'post', u'put', u'patch']
    lookup_field = 'customer'
