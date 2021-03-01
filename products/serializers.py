"""Serializers products."""

# Django REST Framework
from rest_framework import serializers

# Models
from products.models import Category, Product, ProductComment, ProductGallery, ProductReview, ProductVariation


class CategorySerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Category
        fields = ('name_en', 'description_en', 'name_es', 'description_es',
                  'icon', 'picture', 'created_at', 'modified_at', 'author',)
        read_only_fields = ('author', 'created_at', 'modified_at')


class ProductGallerySerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = ProductGallery
        fields = ('product_variation', 'picture')
        read_only_fields = ('author', 'created_at', 'modified_at')


class ProductSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Product
        fields = ('id', 'sku', 'name_en', 'description_en', 'name_es', 'description_es',
                  'category', 'tags', 'post_related', 'video', 'price', 'discount', 'ranking',
                  'created_at', 'modified_at', 'author',)
        read_only_fields = ('author', 'created_at', 'modified_at')


class ProductReviewSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = ProductReview
        fields = ('review', 'stars', 'product',
                  'created_at', 'modified_at', 'author')
        read_only_fields = ('author', 'created_at', 'modified_at')


class ProductCommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = ProductComment
        fields = ('comment', 'comment_related', 'product',
                  'reported', 'created_at', 'modified_at', 'author',)
        read_only_fields = ('author', 'created_at', 'modified_at')


class ProductVariationSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = ProductVariation
        fields = '__all__'
        read_only_fields = ('author', 'created_at', 'modified_at')
