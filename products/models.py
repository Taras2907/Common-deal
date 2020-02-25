from django.db import models
from django.contrib.postgres.fields import JSONField

from users.models import CustomUser


def upload_location(instance, filename):
    return f"{instance.seller.id}/{filename}"


class Product(models.Model):
    seller = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=400)
    manufacturer = models.ForeignKey('Manufacturer', blank=True, null=True, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    attributes = JSONField(blank=True, null=True, default=dict)
    product_subcategory = models.ForeignKey('ProductSubcategory', on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to=upload_location, null=False, blank=False)

    def __str__(self):
        return self.name


class ProductSubcategory(models.Model):
    name = models.CharField(max_length=400)
    product_category = models.ForeignKey('ProductCategory', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "ProductSubcategories"

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "ProductCategories"


class Manufacturer(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name
