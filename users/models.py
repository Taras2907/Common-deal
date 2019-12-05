import uuid
from django.utils.translation import ugettext as _
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from phonenumber_field import modelfields
from creditcards.models import CardNumberField, SecurityCodeField, CardExpiryField


# class Address(models.Model):
#     address_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     street = models.CharField(max_length=100, blank=False, null=False)
#     house_number = models.IntegerField(blank=False, null=False)
#     city = models.CharField(max_length=50, blank=False, null=False)
#     zip_code = models.CharField(blank=False, null=False, validators=[MinLengthValidator(5), MaxLengthValidator(5)])


class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    nick_name = models.CharField(max_length=30, blank=False, null=False)
    creation_date = models.DateTimeField(auto_created=True, auto_now_add=True)
    email = models.EmailField(max_length=50, blank=False, null=False)
    name = models.CharField(max_length=30, blank=False, null=False)
    surname = models.CharField(max_length=50, blank=False, null=False)
    # bank_account = models.IntegerField(validators=[MinLengthValidator(24), MaxLengthValidator(24)])
    # phone = modelfields.PhoneNumberField(null=False, blank=False)
    # address = models.ForeignKey(Address, on_delete=models.CASCADE)



# class CreditCard(models.Model):
#     credit_card_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     card_number = CardNumberField(_('card number'))
#     expiration_date = CardExpiryField(_('expiration date'))
#     security_code = SecurityCodeField(_('security code field'))
