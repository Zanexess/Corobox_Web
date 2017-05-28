from django.contrib import admin
from Stuff.models import Stuff


class StuffModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'uuid', 'owner']

    class Meta:
        model = Stuff


admin.site.register(Stuff, StuffModelAdmin)