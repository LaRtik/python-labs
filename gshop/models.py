from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    #photo = models.ImageField(upload_to="photos/")
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

# Create your models here.
