from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm
from django.contrib.auth.decorators import user_passes_test



def admin_required(user):
    return user.is_superuser

# Create your views here.
def all_products(request):
    """Vue pour afficher tous les produits"""
    products = Product.objects.all()  
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                products = products.annotate(lower_title=Lower('title'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(title__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sorting,
    }
    return render(request, 'store/products.html', context)


def product_detail(request, product_id):
    """Vue pour afficher les détails d'un produit"""
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'store/product_detail.html', context)


@user_passes_test(admin_required)
def add_product(request):
    """Vue pour ajouter un produit"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully')
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'store/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@user_passes_test(lambda user: user.is_superuser)
def update_product(request, product_id):
    """Vue pour mettre à jour un produit"""
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully')
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)

    template = 'store/update_product.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)



@user_passes_test(lambda user: user.is_superuser)
def delete_product(request, product_id):
    """Vue pour supprimer un produit"""
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully')
        return redirect(reverse('products'))
    
    template = 'store/delete_product.html'
    context = {
        'product': product,
    }
    return render(request, template, context)


    
