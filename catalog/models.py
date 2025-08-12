from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField()
    catagory = models.ForeignKey()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_ut = models.DateTimeField(auto_now=True)
