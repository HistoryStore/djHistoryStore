from django.contrib import admin
from .models import *

#ADMINS
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_view',)
    ordering = ('name',)
    search_fields = ('name',)

class PlaceAdmin(admin.ModelAdmin):
    def vendor_name(self, instance):
        return instance.vendor.name
    list_display = ('vendor_name', 'address',)
    ordering = ('address',)
    # search_fields = ('name',)

# Register your models here.
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Place, PlaceAdmin)