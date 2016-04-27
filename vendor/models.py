from django.db import models
from productos.models import Category

# Create your models here.
class Vendor(models.Model):
    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'

    class Admin:
        def __init__(self):
            pass
        list_display = ('name', 'address',)
        ordering = ('name',)
        search_fields = ('name', 'address')


    #Relations
    categories = models.ManyToManyField(Category)

    #Attributes
    name = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=150, blank=False)
    latitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True)
