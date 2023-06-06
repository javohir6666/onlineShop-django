from django.contrib import admin
from .models import Product, Category, Comment, ProductImage, ClotheCategory, Clothes,Colors,ClothesImage, Sizes
# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'created_at', 'category', 'author']
    inlines = [ProductImageInline]
    

class ClothesImageInline(admin.TabularInline):
    model = ClothesImage

class ClothesAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'created_at', 'category']
    inlines = [ClothesImageInline]


admin.site.register(Clothes, ClothesAdmin)
admin.site.register(ClotheCategory)
admin.site.register(ClothesImage)

admin.site.register(Colors)
admin.site.register(Sizes)

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Comment)