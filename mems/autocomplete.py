from dal import autocomplete
from django import forms
from mems.models import Equipment

equipment = forms.ModelChoiceField(
    queryset=Equipment.objects.all(),
    widget=autocomplete.ModelSelect2(url='equipment-autocomplete'))


