from django.contrib import admin
from .models import Product, Category, SubCategory

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'sku',
        'price',
        'image',
    )
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'category',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
