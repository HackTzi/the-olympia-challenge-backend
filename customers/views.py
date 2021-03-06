"""Customer views"""

# Django REST Framework
from rest_framework import viewsets, mixins, exceptions, generics, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from django.contrib.auth.models import User
from customers.models import Customer, ShippingAddress, Currency, Country, Notification

# Serializers
from customers.serializers import (CustomerSerializer, ShippingAddressSerializer, UserSerializer,
                                   CurrencySerializer, CountrySerializer, NotificationSerializer)


class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomerViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'user'

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

    @action(methods=['post', 'get'], detail=True)
    def notification(self, request, pk=None):
        if request.method == 'POST':
            serializer = NotificationSerializer(request.data, context={'request', request})
            serializer.is_valid(raise_exception=True)

            serializer.create(serializer.validated_data)
            return serializer.data

        elif request.method == 'GET':
            notifications = Notification.objects.filter(customer=pk)

            serializer = NotificationSerializer(notifications, many=True)
            return serializer.data


class ShippingAddressViewSet(viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    http_method_names = [u'get', u'post', u'put', u'patch']
    lookup_field = 'customer'


class CurrencyListView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    # permission_classes = (permissions.IsAuthenticated,)


class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    # permission_classes = (permissions.IsAuthenticated,)
