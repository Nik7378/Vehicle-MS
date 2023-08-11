from django.contrib import admin
from app1.models import Vehicle

# Register your models here.

class VehicleMS_Admin(admin.ModelAdmin):
    list_display = ['vehicle_no', 'vehicle_type', 'vehicle_model', 'vehicle_description' ]
    list_filter =   ['vehicle_no', 'vehicle_type', 'vehicle_model', 'vehicle_description' ]
    search_fields =  ['vehicle_no', 'vehicle_type', 'vehicle_model', 'vehicle_description' ]

admin.site.register(Vehicle, VehicleMS_Admin)
admin.site.site_header = "Vehicle MS Admin Panel"
admin.site.site_title = "Vehicles"
admin.site.index_title = "Welcome To Vehicle MS Admin Panel"