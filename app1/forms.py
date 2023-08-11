from django import forms
from .models import Vehicle

class vehicle_details(forms.ModelForm):
    
    vehicle_description = forms.CharField(label='Vehicle Description', widget=forms.Textarea(attrs={"rows":"3"}))

    class Meta:
        model = Vehicle

        #custom label for model form field
        labels = {
            'vehicle_no' : 'Vehicle No',
            'vehicle_type' : 'Vehicle Type',
            'vehicle_model' : 'Vehicle Model',
            'vehicle_description' : 'Vehicle Description',
        }

        fields = '__all__'
