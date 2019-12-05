from django.contrib import admin
from .models import User  #, CreditCard, Address


@admin.register(User)
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
