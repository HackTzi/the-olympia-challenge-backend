"""Serializers products."""

# Django REST Framework
from rest_framework import serializers

# Models
from products.models import (Category, Product, ProductComment, ProductGallery,
                             ProductReview, ProductVariation, Collection)


class CategorySerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name_en', 'name_es', 'picture', 'created_at',
                  'products_count', 'modified_at', 'author',)
        read_only_fields = ('author', 'created_at', 'modified_at')

    def get_products_count(self, category):
        return Product.objects.filter(category=category).count()


class ProductGallerySerializer(serializers.ModelSerializer):
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
        fields = '__all__'
        read_only_fields = ('author', 'created_at', 'modified_at')


class ProductCommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = ProductComment
        fields = '__all__'
        read_only_fields = ('author', 'created_at', 'modified_at')


class ProductVariationSerializer(serializers.ModelSerializer):
    pictures = serializers.SerializerMethodField()

    class Meta:
        model = ProductVariation
        fields = ('product', 'stock', 'color', 'size', 'capabilities', 'main',
                  'pictures', 'created_at', 'modified_at')
        read_only_fields = ('author', 'created_at', 'modified_at')

    def get_pictures(self, product_variation):
        product_variation_pictures = ProductGallery.objects.filter(
            product_variation=product_variation)

        return [i.picture.url for i in product_variation_pictures]


class CollectionSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Collection
        fields = '__all__'
        read_only_fields = ('author', 'created_at', 'modified_at')
