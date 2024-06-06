from django import forms
from .models import Vehicle, VehicleImage

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['name', 'price', 'description', 'power', 'brand', 'condition', 'fuel_type', 'subcategory', 'transmission', 'running_cost']

class VehicleImageForm(forms.ModelForm):
    class Meta:
        model = VehicleImage
        fields = ['image']
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
