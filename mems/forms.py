from django import  forms
from django.forms import DateInput
from dal import autocomplete
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import MultiWidget


# DATE SELECTOR WIDGET
class DateInput(forms.DateInput):
    input_type = 'date'



# FORM FOR EQUIPMENT
class EquipmentForm(forms.ModelForm):

    manufacturer = forms.ModelChoiceField(
                   queryset=Manufacturer.objects.all(),
                   widget=autocomplete.ModelSelect2(url='manufacturer-autocomplete'))

    class Meta:

        model = Equipment


        fields = ('asset_id', 'serial_number', 'manufacturer','model','category','department','purchase_order','cost','accepted_date','warranty_expiry','equipment_status','next_service_date')
        widgets = {'accepted_date': DateInput(),'warranty_expiry': DateInput(),'next_service_date':DateInput(),}



# FORM FOR JOBS
class JobsForm(forms.ModelForm):

    equipment = forms.ModelChoiceField(
                   queryset=Equipment.objects.all(),
                   widget=autocomplete.ModelSelect2(url='equipment-autocomplete'))

    class Meta:
        model = Job


        fields = ('equipment', 'job_department', 'job_type', 'job_status', 'job_date', 'job_description', 'job_work_done','job_time_taken')
        widgets = {'job_date': DateInput()}