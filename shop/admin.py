from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'category',
        'collection',
        'price',
        'is_available',
    )

    list_filter = (
        'category',
        'collection',
        'is_available',
    )

    search_fields = (
        'name',
        'description',
    )