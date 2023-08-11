from django.urls import path
from .import views

urlpatterns=[
    
    path('add', views.add_vehicle, name="add_vehicle"),
    path('edit/<int:rid>', views.edit_vehicle, name="edit_vehicle"),
    path('delete/<int:rid>', views.delete_vehicle, name="delete_vehicle"),
    path('', views.view_all_vehicle, name="view_all_vehicles"),

]
