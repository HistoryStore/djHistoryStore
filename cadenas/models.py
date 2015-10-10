from django.db import models

# Create your models here.
class Place(models.Model):
	name = models.CharField("nombre", max_length=140)
	image = models.ImageField("logo", upload_to="lugares/")
	
	def image_url(self):
		self.image.url

	def __str__(self):
		self.name

	class Admin:
		list_display = ('image', 'name',)
		ordering = ('name',)
		search_fields = ('name',)