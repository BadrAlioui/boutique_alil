from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


# Create your views here.
def all_products(request):
    """Vue pour afficher tous les produits"""
    products = Product.objects.all()  # Récupère tous les produits depuis le modèle
    context = {
        'products': products,  # Passe les produits au template
    }
    return render(request, 'store/products.html', context)