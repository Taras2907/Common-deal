from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from phonenumber_field import modelfields


class Address(models.Model):
    street = models.CharField(max_length=100, blank=False, null=False)
    house_number = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
    zip_code = models.CharField(max_length=5, blank=False, null=False,
                                validators=[MinLengthValidator(5), MaxLengthValidator(5)])


class CustomUser(AbstractUser):
    phone = modelfields.PhoneNumberField(null=False, blank=False)
    bank_account = models.IntegerField(validators=[MinLengthValidator(24), MaxLengthValidator(24)], null=True)
    address = models.ForeignKey("Address", on_delete=models.CASCADE, null=True)
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
