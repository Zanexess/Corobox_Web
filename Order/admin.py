from django.contrib import admin
from Order.models import Order, CategoryOrder


class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'owner']

    class Meta:
        model = Order


class CategoryOrderAdmin(admin.ModelAdmin):
    class Meta:
        model = CategoryOrder


admin.site.register(Order, OrderModelAdmin)
admin.site.register(CategoryOrder, CategoryOrderAdmin)