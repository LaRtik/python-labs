from django.contrib import admin

# Register your models here.
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'photo', 'is_available')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_editable = ('is_available',)
    list_filter = ('is_available', 'category')
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
