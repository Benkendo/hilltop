from django.shortcuts import render, get_object_or_404
from .models import Vehicle, companyLogo

def HomePage(request):
    company_logo = companyLogo.objects.first()
    vehicles = Vehicle.objects.all()
    context = {
        'company_logo': company_logo,
        'vehicles': vehicles,
    }
    return render(request, 'cars/vehicles.html', context)

def vehicle_details(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    return render(request, 'cars/vehicleDetails.html', {'vehicle': vehicle})
