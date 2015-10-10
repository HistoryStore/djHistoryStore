from django.db import models


# Create your models here.
class Category(models.Model):
	name = models.CharField("categoria", max_length=140)
	image = models.ImageField("imagen", upload_to="categorias/")

	def __str__(self):
		self.name
	
	def image_url(self):
		self.image.url

	class Admin:
		list_display = ('image', 'name',)
		ordering = ('name',)
		search_fields = ('name',)

class Product(models.Model):
	barcorde = models.CharField("codigo", max_length=140, null=True, blank=True)
	name = models.CharField("nombre", max_length=140)
	category = models.ForeignKey(Category, verbose_name='categoria')

	def __str__(self):
		self.name


	class Admin:
		list_display = ('barcorde', 'name','category',)
		ordering = ('category','name',)
		search_fields = ('name','category__name',)