from django.contrib import admin
from Order.models import Order


class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'owner']

    class Meta:
        model = Order


admin.site.register(Order, OrderModelAdmin)