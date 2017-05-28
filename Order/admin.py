from django.contrib import admin
from Order.models import Order, CategoryOrder, OrderFrom


class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'owner']

    class Meta:
        model = Order


class OrderFromModelAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'owner']

    class Meta:
        model = OrderFrom


class CategoryOrderAdmin(admin.ModelAdmin):
    class Meta:
        model = CategoryOrder


admin.site.register(Order, OrderModelAdmin)
admin.site.register(CategoryOrder, CategoryOrderAdmin)
admin.site.register(OrderFrom, OrderFromModelAdmin)