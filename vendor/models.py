from django.db import models
from productos.models import Category

# Create your models here.
class Vendor(models.Model):
    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'

    # Relations
    categories = models.ManyToManyField(Category)

    # Attributes
    name = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to='vendor/', blank=True)

    def __str__(self):
        return self.name

    def image_view(self):
        return """
        <img src="%s" style="max-width: 120px; max-height: 120px;" />
        """ % self.image.url

    image_view.allow_tags = True

class Place(models.Model):
    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'

    # Relations
    vendor = models.ForeignKey(Vendor, related_name='places', blank=False)

    # Attributes
    address = models.CharField(max_length=150, blank=False)
    latitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, default=0.000)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, default=0.000)
