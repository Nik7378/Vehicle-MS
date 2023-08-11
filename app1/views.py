from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import vehicle_details
from .models import Vehicle

# Create your views here.

# add new vehicle 
def add_vehicle(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            vehicle_no = request.POST['vehicle_no']
            if not str(vehicle_no).isalnum():
                return HttpResponse("Vehicle No. must be combination of numbers and characters")

            fm = vehicle_details(request.POST)
            if fm.is_valid():
                fm.save()
                return redirect('/')
        else:
            fm = vehicle_details()
        return render(request, "vehicle/add_vehicle.html", {'form':fm})
    else:
        return render(request, 'error.html')

# update existing vehicle 
def edit_vehicle(request, rid):
    if request.user.is_superuser or request.user.is_staff:
        j1 = Vehicle.objects.get(id=rid)
        
        if request.method == 'POST':
            vehicle_no = request.POST['vehicle_no']
            if not str(vehicle_no).isalnum():
                return HttpResponse("Vehicle No. must be combination of numbers and characters")

            fm  = vehicle_details(request.POST, instance=j1)
            if fm.is_valid():
                j1.save()
                return redirect('/')
        else:
            fm = vehicle_details(instance=j1)
        return render(request, 'vehicle/edit_vehicle.html', {'form': fm})
    else:
        return render(request, 'error.html')

# delete existing vehicle 
def delete_vehicle(request, rid):
    if request.user.is_superuser:
        x = Vehicle.objects.get(id=rid)
        x.delete()
        return redirect('/')
    else:
        return render(request, 'error.html')

# view all vehicles 
def view_all_vehicle(request):
    content = {}
    content['data'] = Vehicle.objects.all()
    return render(request, 'vehicle/dashboard.html',content)