from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from productos.models import Product

class List(models.Model):

    class Meta:
        verbose_name = 'List'
        verbose_name_plural = 'Lists'

    #Relations
    user = models.ForeignKey(User, verbose_name="usuario")
    products = models.ManyToManyField(Product, related_name='lists')

    #Attributes
    date_shopping = models.DateField("fecha", auto_now=True)
    status = models.BooleanField("status", default=False)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.date_shopping = timezone.now().date()
        return super(List, self).save(*args, **kwargs)

    # @property
    # def total(self):
    #     products = self.products.all()
    #     dTotal = 0
    #     for product in products:
    #         dTotal += product.total
    #     return dTotal

    def __str__(self):
        return "{0} {1}".format(self.date_shopping, self.user.username)


# class Shopping(models.Model):
#     product = models.ForeignKey(Product, verbose_name="producto", related_name="shoppings",
#                                 related_query_name="shopping")
#     list = models.ForeignKey(List, verbose_name="lista", related_name="shoppings", related_query_name='shopping')
#     price = models.DecimalField("precio", max_digits=6, decimal_places=2)
#     quantity = models.IntegerField("cantidad", default=1)
#
#     @property
#     def total(self):
#         return self.price * self.quantity
#
#     def get_abr_type_uom(self):
#         if self.type_uom == self.KILOGRAM:
#             return "kg" if self.conversion > 0 else "gr"
#         elif self.type_uom == self.LITER:
#             return "lt" if self.conversion > 0 else "ml"
#         else:
#             return "pz"
#
#     def get_conversion_type_uom(self):
#         valor = self.conversion if self.conversion > 0 else self.conversion * 1000
#         return "{0}{1}".format(valor, self.get_abr_type_uom())
#
#     def __str__(self):
#         return "{0} {1} {3}".format(self.product.name, self.get_conversion_type_uom(), self.quantity)