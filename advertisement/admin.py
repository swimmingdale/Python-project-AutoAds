from django.contrib import admin
from advertisement.models import CarBrand, CarModel, Car

class CarAdmin(admin.ModelAdmin):
    search_fields = ['car_model',]
    list_filter = ['car_model__make__name',]
    list_display = ('car_model',)

admin.site.register(CarBrand)
admin.site.register(CarModel)
admin.site.register(Car, CarAdmin)