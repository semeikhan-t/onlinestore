from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductReview)
