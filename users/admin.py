from django.contrib import admin
from .models import CustomUser  #, CreditCard, Address


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    pass
#
#
# @admin.register(CreditCard)
# class CreditCardAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Address)
# class AddressAdmin(admin.ModelAdmin):
#     pass
#
