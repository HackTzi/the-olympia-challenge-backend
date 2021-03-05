"""Customers model"""

# Django
from django.db import models

# Models
from django.contrib.auth.models import User
from customers.models import Customer, ShippingAddress
from products.models import Coupon, Product


class Order(models.Model):
    """Order Model"""
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    shipping_address = models.ForeignKey(
        ShippingAddress, on_delete=models.SET_NULL, null=True)

    products = models.ManyToManyField(Product, through='ProductOrder')
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True)

    products_price = models.FloatField()
    shipping_price = models.FloatField()
    tax_price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class ProductOrder(models.Model):
    """ProductOrder model"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class OrderTracking(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    CHOICES_TYPE = [
        ('awaiting_payment', 'Awaiting payment'),
        ('preparing_shipment', 'milestones'),
        ('on_the_way', 'On the way'),
        ('no_delivery_confirmation', 'No delivery confirmation'),
        ('delivery_refused', 'Delivery refused'),
        ('delivered', 'Delivered'),
    ]

    type = models.CharField(max_length=30, choices=CHOICES_TYPE)
    observations = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)