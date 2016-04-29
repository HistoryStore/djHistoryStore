from django.contrib import admin
from .models import Category, Product, Comment

#ADMINS
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    ordering = ('name',)
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):

    list_display = ('code', 'image_view', 'name', 'category',)
    ordering = ('category', 'name',)
    search_fields = ('name', 'category__name',)

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)