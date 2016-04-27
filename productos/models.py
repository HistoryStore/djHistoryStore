from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    #Relations

    #Attributes
    name = models.CharField("categoria", max_length=140)
    image = models.ImageField("imagen", upload_to="categories/")

    def __str__(self):
        return self.name

    def image_view(self):
        return """
        <img src="%s" style="max-width: 120px; max-height: 120px;" />
        """ % self.image.url

    image_view.allow_tags = True

class Product(models.Model):

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    class Admin:
        def __init__(self):
            pass

        list_display = ('code', 'image_view', 'name', 'category',)
        ordering = ('category', 'name',)
        search_fields = ('name', 'category__name',)

    KILOGRAM = "kilogram"
    LITER = "liter"
    PIECE = "piece"

    CHOICES_TYPE_UOM = ( (KILOGRAM, "Kilogramo"), (LITER, "Litro"), (PIECE, "Pieza"),)

    #Relations
    category = models.ForeignKey(Category, blank=False, verbose_name='categoria', related_name='products')
    # list = models.ForeignKey(List, verbose_name="lista", related_name="products", related_query_name='product',null=True, blank=True)

    #Attributes
    code = models.CharField("codigo", max_length=140, null=True, blank=True)
    name = models.CharField("nombre", max_length=140, blank=False)
    type_uom = models.CharField("tipo uom", max_length=10, choices=CHOICES_TYPE_UOM, default=KILOGRAM, blank=False)
    conversion = models.DecimalField("conversion", max_digits=6, decimal_places=3, default=0, blank=False)
    # price = models.DecimalField("precio", max_digits=6, decimal_places=2, default=0, blank=False)
    # quantity = models.IntegerField("cantidad", default=0, blank=False)

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

    # def __str__(self):
    #     return "{0} {1} {3}".format(self.product.name, self.get_conversion_type_uom(), self.quantity)

    def __str__(self):
        return self.name

    def image_view(self):
        return self.category.image_view()

class Comment(models.Model):

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    class Admin:
        def __init__(self):
            pass

        list_display = ('comment', 'user', 'product', 'qualification',)
        ordering = ('created_at', '-qualification',)
        search_fields = ('user__first_name', 'user__last_name', 'product__name', 'product__category__name',)

    user = models.ForeignKey(User, related_name="comments", related_query_name="comment", blank=False)
    product = models.ForeignKey(Product, related_name="products", related_query_name="product", blank=False)
    comment = models.TextField("comentario", blank=False)
    created_at = models.DateTimeField("creado", auto_now=True)
    qualification = models.IntegerField("calificacion", default=0, blank=False)

    def __str__(self):
        return "User: {0} Product: {1} Qualification: {2}".format(self.user.get_full_name(), self.product, self.qualification)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = timezone.now()
        return super(Comment, self).save(*args, **kwargs)


