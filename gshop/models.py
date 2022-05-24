from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    #photo = models.ImageField(upload_to="photos/")
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}-{id}"

    def get_absolute_url(self):
        return reverse('product', kwargs={"productid": self.id})

# Create your models here.
