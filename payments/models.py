"""Payments model"""

# Django
from django.db import models

# Models
from orders.models import Order
from django.contrib.auth.models import User


class Payment(models.Model):
    """Payment Model"""
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)

    CHOICES_PAYMENT_METHODS = [
        ('credit_card', 'Credit card'),
        ('cash', 'Cash'),
        ('bitcoin', 'Bitcoin'),
        ('paypal', 'Paypal'),
        ('bank_transfer', 'Bank transfer'),
    ]

    payment_method = models.CharField(
        max_length=15, choices=CHOICES_PAYMENT_METHODS)
    approved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
