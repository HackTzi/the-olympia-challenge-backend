"""Product Views"""

# Django REST Framework
from rest_framework import viewsets, permissions, exceptions, views, filters, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

# Models
from products.models import (Category, Product, ProductComment, ProductReview,
                             ProductVariation, CustomerProduct, Coupon)
from customers.models import Customer

# Serializers
from products.serializers import CategorySerializer, ProductCommentSerializer, ProductSerializer, \
    ProductReviewSerializer, ProductVariationSerializer


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class ProductViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'price', 'free_delivery', 'ranking']
    search_fields = ['sku', 'name', 'category',]

    @action(detail=True, methods=['post', 'get'])
    def reviews(self, request, pk=None):
        if request.method == 'POST':
            request.data['product'] = pk
            serializer = ProductReviewSerializer(
                data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data)

        elif request.method == 'GET':
            reviews = ProductReview.objects.filter(product_id=pk)
            serializer = ProductReviewSerializer(reviews, many=True)

            return Response(serializer.data)

    @action(detail=True, methods=['post', 'get'])
    def comments(self, request, pk=None):
        if request.method == 'POST':
            request.data['product'] = pk

            serializer = ProductCommentSerializer(
                data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)

            return Response(serializer.data)

        elif request.method == 'GET':
            comments = ProductComment.objects.filter(product_id=pk)
            serializer = ProductCommentSerializer(comments, many=True)

            return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def variations(self, request, pk=None):
        variations = ProductVariation.objects.filter(product=pk)
        serializer = ProductVariationSerializer(variations)

        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def like(self, request, pk=None):
        try:
            customer = Customer.objects.get(user=pk)
        except Customer.DoesNotExist:
            raise exceptions.NotFound(detail=f'No customer with user id {pk}.')

        customer_product_rel = CustomerProduct.objects.create(customer=customer, product=pk)
        customer_product_rel.like += 1
        customer_product_rel.taste_propensity = 25.0
        customer_product_rel.save()

        product = self.get_queryset()

        serializer = ProductSerializer(product)

        return Response(serializer.data)


class CouponCheckView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk, format=None):
        try:
            coupon = Coupon.objects.get(pk)
        except Coupon.DoesNotExist:
            raise exceptions.NotFound(detail=f'No coupon with id {pk}.')

        if coupon.quantity == 0:
            return Response('The coupon is no valid.')

        return Response('The coupon is valid.')
