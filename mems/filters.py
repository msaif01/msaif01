import django_filters
from .models import *
from django import forms
from django_filters import DateFilter,DateRangeFilter
class JobsFilter(django_filters.FilterSet):



    class Meta:
        model = Job

        fields = ['job_department','job_type','job_status']


