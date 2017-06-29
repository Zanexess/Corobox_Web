from django.contrib import admin
from Profile.models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'phone']

    class Meta:
        model = User


admin.site.register(User, UserAdmin)