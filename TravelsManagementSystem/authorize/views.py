from django.shortcuts import render, redirect
from .form import personAuth, EnqForm, TravelMngSys, AllotmentForm,DriverForm
from .models import Authenticate 
from django.forms.models import model_to_dict
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import pywhatkit 
from datetime import datetime
from django.core.exceptions import MultipleObjectsReturned



def auth(request):
    if request.method == 'POST':
        form = personAuth(request.POST)
        if form.is_valid():
            Uname = form.cleaned_data['name']
            passwrd = form.cleaned_data['password']
            
            if Authenticate.objects.filter(name=Uname, password=passwrd).exists():
                password_lower = passwrd.lower()  # Converting password to lowercase for easier matching
                
                access_types = ['enquiry', 'driver', 'alart', 'owner']  # Types of access
                
                for access in access_types:
                    if access in password_lower:
                        kwargs = {'accesses': access}
                        url = reverse('welcome', kwargs=kwargs)
                        return redirect(url)

            messages.error(request, "Incorrect username or password.")
        else:
            messages.error(request, "Form is invalid. Please check your inputs.")

    form = personAuth()
    return render(request, 'index.html', {'form': form})

#user Access views
@login_required
def welcome(request, accesses):
    access_list = accesses  # Fetching 'accesses' from the URL
    return render(request, 'welcome.html', {'accesses': access_list})


#Enquiry form views
@login_required
def enquiry(request, MobNum):
    try:
        value = TravelMngSys.objects.get(customer_contact=MobNum)
        
        # Check if all fields in the TravelMngSys object are not null
        all_fields_not_null = all(value is not None for field, value in model_to_dict(value).items())
        
        if all_fields_not_null:
            form = EnqForm()
            messages.success(request, "This is our old customer!")
        else:
            # If any field is null, create a new empty form
            form = EnqForm(instance=value)
            
    except TravelMngSys.DoesNotExist:
        form = EnqForm()

    if request.method == 'POST':
        form = EnqForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data saved successfully!")
            return redirect('welcome', accesses='enquiry')
        else:
            messages.error(request, "Form data is invalid.")

    return render(request, 'enquiry.html', {'form': form})


#Trip details views
@login_required
def driver(request, MobNum):
    try:
        # Retrieve the first matching object using .first()
        value = TravelMngSys.objects.filter(customer_contact=MobNum).last()
        if value:
            form = DriverForm(instance=value)

            if request.method == 'POST':
                form = DriverForm(request.POST, instance=value)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Saved data successfully!")
                    return redirect('welcome', accesses='driver')
                else:
                    messages.error(request, "Invalid form data.")
        else:
            messages.error(request, "No matching record found for this contact number.")
            return redirect('welcome', accesses='driver')

    except MultipleObjectsReturned:
        messages.error(request, "Multiple records found for this contact number.")
        # Handle the scenario where multiple records are found
        
    except TravelMngSys.DoesNotExist:
        messages.error(request, "Please enter the correct contact number!")
        return redirect('welcome', accesses='driver')

    return render(request, 'trip_details.html', {'form': form})

    
#Allotment views
@login_required
def allotment(request, MobNum):
    
    try:
        value = TravelMngSys.objects.filter(customer_contact=MobNum).last()
        form = AllotmentForm(instance=value)

        if request.method == 'POST':
            form = AllotmentForm(request.POST, instance=value)
            if form.is_valid():
                form.save()
                messages.success(request, "Data saved successfully!")

                # Prepare the message to be sent
                message = f"Your Taxi is Booked!\nDriver name: {form.cleaned_data['driver_name']}\nDriver Contact: {form.cleaned_data['driver_contact']}\nVehicle No: {form.cleaned_data['vehicle_number']}"

                
                # Send the WhatsApp message
                pywhatkit.sendwhatmsg_instantly(
                    phone_no=str(form.cleaned_data['customer_contact']),
                    message=message,
                    wait_time=25
                )

                # Redirect to 'welcome' on successful booking
                return redirect('welcome', accesses='alart')

            else:
                
                messages.error(request, "Form data is invalid.")
    except TravelMngSys.DoesNotExist:
        messages.error(request, "Please enter the correct Contact number!")
        return redirect('welcome', accesses='alart')

    return render(request, 'allotment.html', {'form': form})


def datatable(request,date):
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    data = TravelMngSys.objects.filter(pickup_date = date_obj).all()

    return render(request, 'datatable.html', {'data':data})


def error_404(request, exception):
    return render(request, '404.html')