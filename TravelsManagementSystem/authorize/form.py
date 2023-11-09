from django import forms
from .models import Authenticate, TravelMngSys
from datetime import date

class personAuth(forms.ModelForm):
    class Meta:
        model = Authenticate
        fields = ['name', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'user name'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'})
        }

class EnqForm(forms.ModelForm):
    total_amount_included = forms.CharField(min_length=20,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Total Amt & inclde all..'}))
    advance_amount = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control','type': 'number','placeholder': 'Enter Adance Payment Amt'}))
    days_trip = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control','type': 'number','placeholder': 'Enter How many days Trip'}))
    
    class Meta:
        model = TravelMngSys
        fields = ('customer_name', 'customer_contact', 'pickup_date', 'drop_date', 'pickup_location', 'visit_places', 'vehicle_type',
                  'total_amount_included', 'advance_amount', 'days_trip', 'total_km')
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer Name'}),
            'customer_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer Contact No:','value':'+91'}),
            'pickup_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Pickup location'}),
            'pickup_date' : forms.DateInput(attrs={'type': 'date','class':'form-control','min': date.today().strftime('%Y-%m-%d')}),
            'drop_date': forms.DateInput(attrs={'type': 'date','class':'form-control','min': date.today().strftime('%Y-%m-%d')}),
            'visit_places': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Visiting Places..'}),
            'vehicle_type': forms.Select(attrs={'class': 'form-control' }),  
            'total_km': forms.TextInput(attrs={'class': 'form-control','type': 'number','placeholder': 'Enter Total runnded KM:'})
                }


class DriverForm(forms.ModelForm):
    vehicle_start_km = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control','type': 'number','placeholder': 'Enter Vehicle Starting Km'}))
    vehicle_close_km = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control','type': 'number','placeholder': 'Enter Vehicle Closing Km'}))
    received_amount = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control','type': 'number','placeholder': 'Enter Received Amount'}))
    
       
    class Meta:
        model = TravelMngSys
        fields = ['customer_name', 'customer_contact','vehicle_start_km','vehicle_close_km','received_amount','drop_location','drop_date', 'total_km']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'readonly':True}),
            'customer_contact': forms.TextInput(attrs={'class': 'form-control', 'readonly':True}),
            'drop_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Drop location'}),
            'drop_date': forms.DateInput(attrs={'type': 'date','class':'form-control'}), 
            'total_km': forms.TextInput(attrs={'class': 'form-control','type': 'number','placeholder': 'Enter Total runnded KM:'})
             }
        

class AllotmentForm(forms.ModelForm):
    
    class Meta:
        model = TravelMngSys
        fields = ['customer_name', 'customer_contact', 'pickup_date', 'drop_date', 'pickup_location', 
                'visit_places', 'vehicle_type','days_trip','driver_name','driver_contact','vehicle_number']
        exclude = ['pickup_date']       
          
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'readonly':True}),
            'customer_contact': forms.TextInput(attrs={'class': 'form-control', 'readonly':True}),
            'pickup_date' : forms.DateInput(attrs={'type': 'date','class':'form-control','readonly':True}),
            'drop_date': forms.DateInput(attrs={'type': 'date','class':'form-control','readonly':True}),
            'visit_places': forms.TextInput(attrs={'class': 'form-control', 'readonly':True}),
            'vehicle_type': forms.TextInput(attrs={'class': 'form-control', 'readonly':True}),
            'days_trip': forms.TextInput(attrs={'class': 'form-control', 'readonly':True}),
            'pickup_location': forms.TextInput(attrs={'class': 'form-control', 'readonly':True}),
            'driver_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Driver Name: '}),
            'driver_contact':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer Contact Num..','value':'+91'}),
            'vehicle_number':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vehicle No: '})
        }
