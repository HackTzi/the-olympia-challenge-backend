"""Customers model"""

# Django
from django.db import models

# Models
from django.contrib.auth.models import User


class Currency(models.Model):
    """Currency Model"""
    abbreviation = models.CharField(max_length=3)
    name = models.CharField(max_length=40)
    USD_equivalence = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'currencies'

    def __str__(self):
        return f'{self.name} [{self.abbreviation}]'


class Country(models.Model):
    """Country Model"""
    name = models.CharField(max_length=40)
    tax_rate = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'countries'


class Customer(models.Model):
    """Customer model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='customers/pictures/', null=True, blank=True)

    CHOICES_WORK_AREA = [
        ('software_development', 'Software development'),
        ('marketing', 'Marketing'),
        ('design', 'Design'),
        ('gamer', 'Gamer'),
        ('product_management', 'Product management'),
        ('other', 'Other')
    ]

    work_area = models.CharField(max_length=30, choices=CHOICES_WORK_AREA)

    CHOICES_PREFERENCES = [
        ('minimalistic', 'Minimalistic'),
        ('with_rgb', 'With RGB'),
        ('multiscreen', 'Multiscreen'),
        ('small', 'Small'),
        ('gamer', 'Gamer'),
        ('office', 'Office'),
    ]

    preferences = models.CharField(max_length=30, choices=CHOICES_PREFERENCES)

    CHOICES_LANGUAGE = [
        ('es', 'Español'),
        ('en', 'English'),
    ]

    language = models.CharField(max_length=5, choices=CHOICES_LANGUAGE)
    phone_number = models.CharField(max_length=30)

    currency = models.ForeignKey(
        Currency, on_delete=models.SET_NULL, null=True)
    points = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return self.user.get_full_name()


class ShippingAddress(models.Model):
    """Shipping address Model"""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

    country = models.ForeignKey(Country, models.SET_NULL, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.address


class Notification(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
