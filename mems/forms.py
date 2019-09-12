from django import  forms
from .models import *

class EquipmentForm(forms.ModelForm):
    class Meta:

        model = Equipment
        fields = ('asset_id', 'serial_number', 'manufacturer','category','department','purchase_order')



class JobsForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('job_number', 'equipment', 'job_department', 'job_type', 'job_status', 'job_description', 'job_work_done','job_time_taken')
