from django.db import models
from django.urls import reverse
#from django.utils.translation import gettext as translated


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование продукта")
    description = models.TextField(verbose_name="Описание продукта")
    price = models.FloatField(verbose_name="Цена")
    photo = models.ImageField(upload_to=f"photos/", null=True, verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    is_published = models.BooleanField(default=True, verbose_name="В наличии")
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True, verbose_name="Категория")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={"productid": self.pk})

    class Meta:
        verbose_name = "Продукты"
        verbose_name_plural = "Продукты"
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=180, db_index=True, verbose_name="Тип продукта")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.id})

    class Meta:
        verbose_name = "Тип продукта"
        verbose_name_plural = "Типы продуктов"
        ordering = ['name']

# Create your models here.
