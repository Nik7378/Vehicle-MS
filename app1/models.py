from django.db import models

# Create your models here.

class Vehicle(models.Model):

    vehicle_type_options = [
        ('Two Wheelers', 'Two Wheelers'),
        ('Three Wheelers', 'Three Wheelers'),
        ('Four Wheelers', 'Four Wheelers'),
    ]

    vehicle_no = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=50, choices=vehicle_type_options, default=vehicle_type_options)
    vehicle_model = models.CharField(max_length=50)
    vehicle_description = models.TextField(max_length=1000)