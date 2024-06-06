from django.contrib import admin
from .models import Manufacturer, Brand, Category, SubCategory, Condition, FuelType, Transmission, Vehicle, VehicleImage,companyLogo

class VehicleImageInline(admin.TabularInline):
    model = VehicleImage
    extra = 1

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    inlines = [VehicleImageInline]

admin.site.register(Manufacturer)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Condition)
admin.site.register(FuelType)
admin.site.register(Transmission)
admin.site.register(VehicleImage)
admin.site.register(companyLogo)
