from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField("categoria", max_length=140)
    image = models.ImageField("imagen", upload_to="categories/")

    def __str__(self):
        return self.name

    def image_view(self):
        return """
        <img src="%s" style="max-width: 120px; max-height: 120px;" />
        """ % (self.image.url)

    image_view.allow_tags = True

    class Admin:
        def __init__(self):
            pass

        list_display = ('image_view', 'name',)
        ordering = ('name',)
        search_fields = ('name',)


class Product(models.Model):
    key = models.CharField("codigo", max_length=140, null=True, blank=True)
    name = models.CharField("nombre", max_length=140)
    category = models.ForeignKey(Category, verbose_name='categoria')

    def __str__(self):
        return self.name

    def image_view(self):
        return self.category.image_view()

    class Admin:
        def __init__(self):
            pass

        list_display = ('key', 'image_view', 'name', 'category',)
        ordering = ('category', 'name',)
        search_fields = ('name', 'category__name',)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comments", related_query_name="comment")
    product = models.ForeignKey(Product, related_name="products", related_query_name="product")
    comment = models.TextField("comentario")
    created_at = models.DateTimeField("creado", auto_created=True)
    qualification = models.IntegerField("calificacion", default=0)

    def __str__(self):
        return "User: {0} Product: {1} Qualification: {2}".format(self.user.get_full_name(), self.product,
                                                                  self.qualification)

    class Admin:
        def __init__(self):
            pass

        list_display = ('comment', 'user', 'product', 'qualification',)
        ordering = ('created_at', '-qualification',)
        search_fields = ('user__first_name', 'user__last_name', 'product__name', 'product__category__name',)