from django.contrib import admin
from .models import Product, Category, Comment, ProductImage
# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'created_at', 'category', 'author']
    inlines = [ProductImageInline]
    
admin.site.register(Category)

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Comment)