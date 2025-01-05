from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.all_products, name='products'),
    path('add/', views.add_product, name='add_product'),
    path('product/<product_id>/update/', views.update_product, name='update_product'),
    path('product/<product_id>/delete/', views.delete_product, name='delete_product'),
    path('product/<product_id>/', views.product_detail, name='product_detail'),
]