from django import  forms
from .models import *

class EquipmentForm(forms.ModelForm):
    class Meta:

        model=Equipment
        fields=('assetId', 'manufacturer','category','department','purchaseOrder')


