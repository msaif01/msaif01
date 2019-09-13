from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def index(request):
    return render(request,'index.html')

# Create your views here.

def display_jobs(request):
    jobs = Job.objects.all()
    context = {
        'jobs': jobs,
        'header': 'Job',
    }
    return render(request, 'view_all_jobs.html', context)



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
          return redirect('display_jobs')

    else:
        form = JobsForm()
        return render(request, 'add_jobs.html', {'form': form})


def job_edit(request, job_number=None):
    instance = get_object_or_404(Job, job_number=job_number)
    form = JobsForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('display_jobs')


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