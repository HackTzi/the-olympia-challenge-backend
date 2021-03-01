"""Products admin config."""

# Django
from django.contrib import admin

# Nested Inline
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

# Models
from products.models import Product, Category, ProductVariation, ProductGallery


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'description_en', 'created_at',
                    'modified_at', 'author')
    list_display_links = ('name_en', 'description_en',)
    search_fields = ('name',)
    readonly_fields = ('author', 'created_at', 'modified_at')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


class ProductGalleryInline(NestedStackedInline):
    model = ProductGallery
    readonly_fields = ('created_at', 'modified_at')
    extra = 0


class ProductVariationInline(NestedStackedInline):
    model = ProductVariation
    extra = 0
    min_num = 1
    readonly_fields = ('created_at', 'modified_at')

    inlines = [ProductGalleryInline]


@admin.register(Product)
class ProductAdmin(NestedModelAdmin):
    list_display = ('sku', 'name_en', 'price', 'category', 'ranking')
    list_display_links = ('sku', 'name_en', 'price', 'category', 'ranking')
    search_fields = ('sku', 'name_en', 'price', 'category')
    list_filter = ('category',)
    readonly_fields = ('author', 'created_at', 'modified_at', 'ranking')
    list_per_page = 30

    inlines = [ProductVariationInline]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()
