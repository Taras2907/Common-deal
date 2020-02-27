from django.db import models
from django.contrib.postgres.fields import JSONField

from users.models import CustomUser
from .media_locations import upload_location, upload_location_main_image


class Product(models.Model):
    seller = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=400)
    manufacturer = models.ForeignKey('Manufacturer',default=None, blank=True, null=True, on_delete=models.SET_DEFAULT)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    attributes = JSONField(blank=True, null=True, default=dict)
    product_subcategory = models.ForeignKey('ProductSubcategory',default=None, on_delete=models.SET_DEFAULT,  related_name='subcategory')
    expiration_date = models.DateTimeField()
    image = models.ImageField(upload_to=upload_location_main_image, null=False, blank=False)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to=upload_location, null=False, blank=False)
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="images")


class ProductSubcategory(models.Model):
    name = models.CharField(max_length=400)
    product_category = models.ForeignKey('ProductCategory', on_delete=models.DO_NOTHING, related_name='subcategories')

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
    name = models.CharField(max_length=400, unique=True)

    def __str__(self):
        return self.name
