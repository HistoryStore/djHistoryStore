from django.contrib import admin
from .models import Category, Product, Comment

#ADMINS
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_view')
    ordering = ('name',)
    search_fields = ('name',)

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
admin.site.register(Comment)