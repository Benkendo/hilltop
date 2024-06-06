from django.db import models
from django.contrib.auth.models import User

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Condition(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FuelType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Transmission(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    year_of_manufacture = models.PositiveIntegerField(default=2000)
    description = models.TextField(null=True, blank=True)
    power = models.PositiveIntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    condition = models.ForeignKey(Condition, on_delete=models.SET_NULL, null=True, blank=True)
    fuel_type = models.ForeignKey(FuelType, on_delete=models.SET_NULL, null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True)
    transmission = models.ForeignKey(Transmission, on_delete=models.SET_NULL, null=True, blank=True)
    running_cost = models.PositiveIntegerField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicles')

    def __str__(self):
        return self.name

class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='vehicle_images/')

    def __str__(self):
        return f"Image for {self.vehicle.name}"

    
class companyLogo(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    logo = models.ImageField(upload_to='company_logos/')