from django.shortcuts import render
from django.views import View
from products.models import Product, Category, ClotheCategory,Clothes
from django.shortcuts import get_object_or_404
from users.models import Saved
import random


def for_all_pages(request):
    categories = Category.objects.all()
    clotheCategory = ClotheCategory.objects.all()
    items = list(Category.objects.all())
    random_items = random.sample(items, 3)
    return {
            'categories': categories,
            'random_items': random_items,
            'clotheCategory':clotheCategory
            }


class IndexView(View):
    def get(self, request):
        items2 = list(ClotheCategory.objects.all())
        categories = Category.objects.all()[:8]
        products = Product.objects.all()
        random_items2 = random.sample(items2, 3)
        return render(request, 'pages/index.html', {
            'products': products,
            'random_items2': random_items2,
            'categories': categories,
        })


class CategoryView(View):
    def get(self, request, category_name):
        category = get_object_or_404(Category, name=category_name)
        products = Product.objects.filter(category=category)
        return render(request, 'pages/category.html', {'category': category,
                                                       'products': products})
    
class ClotheCategoryView(View):
    def get(self, request, clotheCategory_title):
        category = get_object_or_404(ClotheCategory, title=clotheCategory_title)
        products = Clothes.objects.filter(category = category)
        return render(request, "pages/clotheCategory.html", {
            'category':category,
            'products':products
        })