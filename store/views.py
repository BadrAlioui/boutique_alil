from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


# Create your views here.
def all_products(request):
    """Vue pour afficher tous les produits"""
    products = Product.objects.all()  
    context = {
        'products': products,  
    }
    return render(request, 'store/products.html', context)


def product_detail(request, product_id):
    """Vue pour afficher les détails d'un produit"""
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'store/product_detail.html', context)