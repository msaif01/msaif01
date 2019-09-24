from django.http import HttpResponse
from mems.models import Manufacturer
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.views import View
from django.views.generic import ListView,DetailView
from .tables import JobsTable
from .filters import JobsFilter
from dal import autocomplete


def index(request):
    return render(request,'index.html')

# Create your views here.

def display_jobs(request):
    jobs = Job.objects.all()
    context = {
        'jobs': jobs,
        'header': 'Job',
    }
    return render(request, 'display_jobs.html', context)



def display_equipment(request):
    items = Equipment.objects.all()
    context = {
        'items': items,
        'header': Equipment,
    }
    return render(request, 'index.html', context)

def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('display_equipment')

    else:
        form = cls()
        return render(request, 'add_equipment.html', {'form': form})


def add_equipment(request):
    return add_item(request, EquipmentForm)


def add_jobs(request):
    if request.method == 'POST':
        form = JobsForm(request.POST)

        if form.is_valid():
          job = form.save(commit=False)
          job.save()
          instance = job
          return redirect('job_view', instance.job_number)

    else:
        form = JobsForm()
        return render(request, 'add_jobs.html', {'form': form})


def edit_job(request, job_number=None):
    instance = get_object_or_404(Job, job_number=job_number)
    form = JobsForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('job_view', job_number)


    context = {
            "title": 'Edit ' + str(instance.job_number),
            "instance": instance,
            "form": form,
            "job_number": job_number,

        }
    return render(request, "edit_job.html", context)




def job_view(request,job_number=None):
    instance = get_object_or_404(Job, job_number=job_number)

    context = {
        'job_number': job_number,
        'instance': instance,
    }
    return render(request,"job_view.html", context)




class JobsListView(ListView):
    model = Job
    template_name = 'JobListView.html'

    def get_context_data(self,**kwargs):
         context = super().get_context_data(**kwargs)
         context['filter'] = JobsFilter(self.request.GET , queryset=self.get_queryset())
         return context




# Autocomplete Classes


class ManufacturerAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = Manufacturer.objects.all()

        if self.q:
            qs = qs.filter(manufacturer_name__istartswith=self.q)
        return qs


class EquipmentAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = Equipment.objects.all()

        if self.q:
            qs = qs.filter(asset_id__istartswith=self.q)
        return qs