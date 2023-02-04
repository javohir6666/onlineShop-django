from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'pages/product_detail.html', {'product': product})