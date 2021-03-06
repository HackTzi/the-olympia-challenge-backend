"""Orders admin configuration."""

# Django
from django.contrib import admin

# Models
from orders.models import Order, OrderTracking, Payment


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderTracking)
class OrderTrackingAdmin(admin.ModelAdmin):
    pass


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass
