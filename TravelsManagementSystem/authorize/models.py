from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

class Authenticate(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
class TravelMngSys(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_contact = PhoneNumberField(region='IN')
    pickup_date = models.DateField(default=timezone.now)
    drop_date = models.DateField(default=timezone.now)
    pickup_location = models.CharField(max_length=50)
    drop_location = models.CharField(max_length=50)
    visit_places = models.CharField(max_length=500)
    
    SEDAN = 'Sedan'
    SUV = 'SUV'
    TEMPO = 'Tempo'
    OTHERS = 'Others'
    VEHICLE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (TEMPO, 'Tempo'),
        (OTHERS, 'Others')
    ]
    vehicle_type = models.CharField(max_length=50, choices=VEHICLE_CHOICES, default=OTHERS)
    
    total_amount_included = models.CharField(max_length=500)
    advance_amount = models.IntegerField(null=True, blank=True)  
    days_trip = models.IntegerField(null=True, blank=True)
    driver_name = models.CharField(max_length=50)
    driver_contact = PhoneNumberField(region='IN')
    vehicle_number = models.CharField(max_length=50)
    vehicle_start_km = models.IntegerField(null=True, blank=True)
    vehicle_close_km = models.IntegerField(null=True, blank=True)
    total_km = models.IntegerField(null=True, blank=True)
    received_amount = models.IntegerField(null=True, blank=True)
