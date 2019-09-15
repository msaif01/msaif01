from django import  forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class EquipmentForm(forms.ModelForm):
    class Meta:

        model = Equipment
        fields = ('asset_id', 'serial_number', 'manufacturer','category','department','purchase_order')

class DateInput(forms.DateInput):
        input_type = 'date'

class JobsForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('job_number', 'equipment', 'job_department', 'job_type', 'job_status', 'job_date', 'job_description', 'job_work_done','job_time_taken')
        widgets = {'job_date': DateInput()}