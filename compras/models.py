from django.db import models
from cadenas.models import Vendor, Place
from django.contrib.auth.models import User
from productos.models import Product
from django.utils import timezone


class List(models.Model):
    date_shopping = models.DateField("fecha", null=True, blank=True, editable=False)
    vendor = models.ForeignKey(Vendor, verbose_name="cadena", related_name="vendors", related_query_name="vendor")
    place = models.ForeignKey(Place, verbose_name="lugar", related_name="places", related_query_name="place")
    status = models.BooleanField("status", default=False)
    user = models.ForeignKey(User, verbose_name="usuario")

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.date_shopping = timezone.now().date()
        return super(List, self).save(*args, **kwargs)

    @property
    def total(self):
        shoppigns = self.shopping_set.all()
        dTotal = 0
        for shopping in shoppigns:
            dTotal += shopping.total
        return dTotal

    def __str__(self):
        return "{0} {1} {2}".format(self.date_shopping, self.place.name, self.total)


class Shopping(models.Model):
    KILOGRAM = "kilogram"
    LITER = "liter"
    PIECE = "piece"

    CHOICES_TYPE_UOM = ( (KILOGRAM, "Kilogramo"), (LITER, "Litro"), (PIECE, "Pieza"),)

    product = models.ForeignKey(Product, verbose_name="producto", related_name="shoppings",
                                related_query_name="shopping")
    list = models.ForeignKey(List, verbose_name="lista", related_name="shoppings", related_query_name='shopping')
    type_uom = models.CharField("tipo uom", max_length=10, choices=CHOICES_TYPE_UOM, default=KILOGRAM)
    price = models.DecimalField("precio", max_digits=6, decimal_places=2)
    conversion = models.DecimalField("conversion", max_digits=6, decimal_places=3)
    quantity = models.IntegerField("cantidad", default=1)

    @property
    def total(self):
        return self.price * self.quantity

    def get_abr_type_uom(self):
        if self.type_uom == self.KILOGRAM:
            return "kg" if self.conversion > 0 else "gr"
        elif self.type_uom == self.LITER:
            return "lt" if self.conversion > 0 else "ml"
        else:
            return "pz"

    def get_conversion_type_uom(self):
        valor = self.conversion if self.conversion > 0 else self.conversion * 1000
        return "{0}{1}".format(valor, self.get_abr_type_uom())

    def __str__(self):
        return "{0} {1} {3}".format(self.product.name, self.get_conversion_type_uom(), self.quantity)