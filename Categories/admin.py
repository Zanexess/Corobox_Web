from django.contrib import admin
from Categories.models import Category


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'max_weight', 'monthly_price']

    class Meta:
        model = Category


admin.site.register(Category, CategoryModelAdmin)