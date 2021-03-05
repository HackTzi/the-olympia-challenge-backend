"""Products model"""

# Django
from django.db import models

# Models
from customers.models import Customer
from django.contrib.auth.models import User

# Utils
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):
    """Category Model"""
    name_es = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)

    picture = models.ImageField(upload_to='categories/pictures/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name_en


class Product(models.Model):
    """Product Model"""
    sku = models.CharField(max_length=15, unique=True)
    name_es = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    description_es = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = ArrayField(models.CharField(max_length=40))

    post_related = models.URLField(null=True, blank=True)
    video = models.FileField(
        upload_to='product/videos/', null=True, blank=True)

    price = models.FloatField()
    discount = models.PositiveIntegerField(default=0)

    free_delivery = models.BooleanField(default=False)
    ranking = models.FloatField(max_length=10.0, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def convert_price_to_currency(self, currency):
        return 0

    def __str__(self):
        return self.name_en


class ProductVariation(models.Model):
    """Product variation model"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()

    color = models.CharField(max_length=7, null=True, blank=True)
    size = models.CharField(max_length=30, null=True, blank=True)
    capabilities = models.CharField(max_length=30, null=True, blank=True)

    main = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product} -> variation #{self.id}' or ''


class ProductGallery(models.Model):
    """Product Gallery Model"""
    product_variation = models.ForeignKey(
        ProductVariation, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='products/pictures/')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_variation or ''


class ProductComment(models.Model):
    comment = models.TextField()
    comment_related = models.ForeignKey(
        'ProductComment', on_delete=models.CASCADE, null=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reported = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class ProductReview(models.Model):
    review = models.TextField()
    stars = models.IntegerField(default=0)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.review


class Coupon(models.Model):
    code = models.CharField(max_length=12, unique=True)
    quantity = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.code


class CustomerProduct(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    taste_propensity = models.FloatField()
    like = models.BooleanField()

    def __str__(self):
        return str(f'{self.customer} -> {self.product}')


class Collection(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='collections/pictures/')

    products = models.ManyToManyField(Product)
    likes = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.customer} collection #{self.id}'
