from django.db import models


# Create your models here.

# class Product(models.Model):
#     name = models.CharField(max_length=200)
#     price = models.IntegerField()
#     description = models.TextField()
#     image = models.ImageField(upload_to='product/', null=True, blank=True)
#
#     def __str__(self):
#         return self.name


class Shop(models.Model):
    name = models.CharField(max_length=150)
    title = models.TextField()
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='shop/', null=True)

    def __str__(self):
        return self.name
