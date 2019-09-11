from django import  forms
from .models import *

class EquipmentForm(forms.ModelForm):
    class Meta:

        model = Equipment
        fields = ('assetId', 'serialNumber', 'manufacturer','category','department','purchaseOrder')



class JobsForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('job_number', 'equipment', 'job_type', 'job_status', 'job_description', 'job_work_done')
