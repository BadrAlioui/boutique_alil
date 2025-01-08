from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=250, unique=True, default="default-slug")

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default='un-branded')
    description = models.TextField()
    slug = models.SlugField(max_length=250, unique=True, default="default-slug")
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(0.1)])
    image = models.ImageField(upload_to='images/', null = True, blank=True)
    stock = models.IntegerField(default=0, blank=True, verbose_name="Stock du produit")

    class Meta:
        verbose_name_plural = "products"

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.TextField()
    reference = models.CharField(max_length=128)
    date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255, default="Created")
    price = models.FloatField(default=0.0, blank=True)
    

    def __str__(self):
        return f"Order by {self.user.username} - Status: {self.status}"

    