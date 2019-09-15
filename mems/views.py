from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.views.generic import ListView
import django_tables2 as SimpleTable
from django_tables2 import SingleTableView
from .tables import JobsTable

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


def job_edit(request, job_number=None):
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
    return render(request, "job_edit.html", context)

def job_view(request,job_number=None):
    instance = get_object_or_404(Job, job_number=job_number)

    context = {
        'job_number': job_number,
        'instance': instance,
    }
    return render(request,"job_view.html", context)


def table_view(request):
    table = JobsTable(Job.objects.all())
    table.paginate(page=request.GET.get("page", 1), per_page=50)

    return render(request,"simple_list.html", {"table": table})