from django.contrib import admin
from . import models

class HotelInline(admin.TabularInline):
    model = models.hotel

class CityAdmin(admin.ModelAdmin):
    inlines = [
        HotelInline,
    ]

admin.site.register(models.City, CityAdmin)
admin.site.register(models.hotel)
admin.site.register(models.tour)