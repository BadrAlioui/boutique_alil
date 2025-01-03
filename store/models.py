from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default='un-branded')
    description = models.TextField()
    slug = models.SlugField(max_length=250)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(0.1)])
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = CloudinaryField('image', null=True, blank=True)

    class Meta:
        verbose_name_plural = "products"

    def __str__(self):
        return self.name