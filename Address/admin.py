from django.contrib import admin
from Address.models import Address


class AddressModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'street', 'house', 'access', 'floor', 'flat', 'owner']

    class Meta:
        model = Address


admin.site.register(Address, AddressModelAdmin)