from django import forms
from weatherapp.models import City

class CityTab(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'City name'})
        }