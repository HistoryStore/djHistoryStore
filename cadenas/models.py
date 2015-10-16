from django.db import models


class Vendor(models.Model):
    name = models.CharField("vendor", max_length=140)
    image = models.ImageField("logo", upload_to="vendor/")

    def image_view(self):
        return """
        <img src="%s" style="max-width: 120px; max-height: 120px;" />
        """ % (self.image.url)

    image_view.allow_tags = True

    def __str__(self):
        return self.name

    class Admin:
        def __init__(self):
            pass

        list_display = ('image_view', 'name',)
        ordering = ('name',)
        search_fields = ('name',)


class Place(models.Model):
    name = models.CharField("nombre", max_length=140)
    #  image = models.ImageField("logo", upload_to="places/")
    vendor = models.ForeignKey(Vendor, verbose_name="vendor", related_query_name="vendor", null=True, blank=True)
    latitude = models.CharField("latitude", max_length="50", null=True, blank=True)
    longitude = models.CharField("longitude", max_length="50", null=True, blank=True)

    def image_view(self):
        return """
        <img src="%s" style="max-width: 120px; max-height: 120px;" />
        """ % (self.image.url)

    image_view.allow_tags = True

    def __str__(self):
        return self.name

    class Admin:
        def __init__(self):
            pass

        list_display = ('name','latitude', 'longitude',)
        ordering = ('name',)
        search_fields = ('name','latitude', 'longitude',)
