from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    search_fields = ("name",)
    readonly_fields = ("slug",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "category",
        "price",
        "quantity",
        "is_featured",
        "is_active",
        "created_at",
    )

    list_filter = (
        "category",
        "is_featured",
        "is_active",
    )

    search_fields = (
        "name",
        "description",
        "short_description",
    )

    readonly_fields = (
        "slug",
        "created_at",
        "updated_at",
    )

    list_editable = (
        "price",
        "quantity",
        "is_featured",
        "is_active",
    )

    ordering = ("-created_at",)