from django.db.models import Model
from django.shortcuts import render
from django.conf import settings

from .models import Products, Category
from collections import defaultdict

def index(request):
    products = Products.objects.select_related('category').all()

    category_products = defaultdict(list)

    for product in products:
        category_products[product.category].append(product)

    category_products = dict(category_products)
    return render(request, 'index.html', {'category_products': category_products, 'base_dir': settings.BASE_DIR}, )