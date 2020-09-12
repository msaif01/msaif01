from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponseRedirect
from mems.models import Equipment, Job
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.views import View
from django.views.generic import ListView, DetailView
from .tables import JobsTable
from .filters import JobsFilter
from dal import autocomplete
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.db.models import Count
import datetime
from datetime import timedelta
from django.db.models import F
from django.utils.datetime_safe import date


def index(request):
    e = Equipment.objects.all()

    # Update PPM due days on page load
    for obj in e:
        obj.next_service_date = obj.service_date + datetime.timedelta(days=obj.ppm_intervel)
        obj.ppm_due_days = (obj.next_service_date - date.today()).days
        obj.save()

    return render(request, 'index.html')


# ----------------VIEWS RELATED TO EQUIPMENT MODEL

def display_equipments(request):
    equipments = Equipment.objects.all()

    context = {
        'equipments': equipments,
        'header': Equipment,
    }
    return render(request, 'display_equipments', context)


def add_equipment(request):
    if request.method == "POST":
        form = EquipmentForm(request.POST)

        if form.is_valid():
            equipment = form.save(commit=False)
            equipment.category_id = equipment.model.model_category_id
            equipment.risk_score = equipment.category.category_risk_score + equipment.department.department_risk_score
            if equipment.risk_score > 6:
                equipment.ppm_intervel = 180
            else:
                equipment.ppm_intervel = 365
            equipment.next_service_date = equipment.accepted_date + datetime.timedelta(days=equipment.ppm_intervel)
            delta = (equipment.next_service_date - equipment.accepted_date).days
            equipment.ppm_due_days = delta

            equipment.save()
            instance = equipment

            i = Equipment.objects.get(pk=instance.asset_id)
            i.risk_score = i.category.category_risk_score + i.department.department_risk_score
            i.save()

            return redirect('view_equipment', instance.asset_id)

    else:
        form = EquipmentForm()
        return render(request, 'add_equipment.html', {'form': form})


def view_equipment(request, asset_id=None):
    instance = get_object_or_404(Equipment, asset_id=asset_id)
    equipment_jobs = Job.objects.all().filter(equipment=asset_id)
    context = {
        'asset_id': asset_id,
        'instance': instance,
        'equipment_jobs': equipment_jobs,
    }
    return render(request, "view_equipment.html", context)


def edit_equipment(request, asset_id=None):
    instance = get_object_or_404(Equipment, asset_id=asset_id)
    form = EquipmentForm(request.POST or None, instance=instance)
    if form.is_valid():
        equipment = form.save(commit=False)

        equipment.category_id = equipment.model.model_category_id
        equipment.risk_score = equipment.category.category_risk_score + equipment.department.department_risk_score
        if equipment.risk_score > 6:
            equipment.ppm_intervel = 180
        else:
            equipment.ppm_intervel = 365
        equipment.next_service_date = equipment.service_date + datetime.timedelta(days=equipment.ppm_intervel)
        d = (equipment.next_service_date - date.today()).days

        equipment.ppm_due_days = d

        equipment.save()
        instance = equipment
        i = Equipment.objects.get(pk=instance.asset_id)
        i.risk_score = i.category.category_risk_score + i.department.department_risk_score
        i.save()

        return redirect('view_equipment', asset_id)

    context = {
        "title": 'Edit ' + str(instance.asset_id),
        "instance": instance,
        "form": form,
        "asset_id": asset_id,

    }
    return render(request, "edit_equipment.html", context)


# ----------------VIEWS RELATED TO JOB MODEL

def add_jobs(request):
    if request.method == 'POST':
        form = JobsForm(request.POST, request.FILES)

        if form.is_valid():
            job = form.save(commit=False)
            instance = job
            form.save()

            if (instance.job_service_done == True):
                device = Equipment.objects.get(pk=instance.equipment_id)
                device.service_date = instance.job_finished_date
                device.next_service_date = device.service_date + datetime.timedelta(days=device.ppm_intervel)
                device.save()

                # asset_update_service= Equipment.objects.get(pk,instance.equipment_id)
                # asset_update_service.service_date= F(instance.job_finished_date)
                # asset_update_service.save()
                # Equipment.objects.filter(pk=instance.equipment_id).update(service_date=instance.job_finished_date)

        return redirect('view_job', instance.job_number)

    else:
        form = JobsForm()
    return render(request, 'add_jobs.html', {'form': form})


def edit_job(request, job_number=None):
    instance = get_object_or_404(Job, job_number=job_number)
    form = JobsForm(request.POST or request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        form.save()
        instance.save()

        if (instance.job_service_done == True):
            device = Equipment.objects.get(pk=instance.equipment_id)
            device.service_date = instance.job_finished_date
            device.next_service_date = device.service_date + datetime.timedelta(days=device.ppm_intervel)
            device.save()

        return redirect('view_job', job_number)

    context = {
        "title": 'Edit ' + str(instance.job_number),
        "instance": instance,
        "form": form,
        "job_number": job_number,

    }
    return render(request, "edit_job.html", context)


def view_job(request, job_number=None):
    instance = get_object_or_404(Job, job_number=job_number)
    instance.job_cost = (instance.job_time_taken * 1)
    context = {
        'job_number': job_number,
        'instance': instance,
    }
    return render(request, "view_job.html", context)


# def display_jobs_json(request):
#   jsonjobs=list(Job.objects.values())
#  return JsonResponse(jsonjobs, safe=False)


# def display_jobs_json(request):
#   jsonjobs = Job.objects.all()
#  jsonjobs = json.dumps(list(jsonjobs), cls=DjangoJSONEncoder)

# context = {'jsonjobs': jsonjobs,
#  'header': Job}
# return HttpResponse(jsonjobs, content_type='application/json')

# def supjson(request):
#   suppliers_all = Supplier.objects.all().values('name', 'classification')
#  suppliers_all = json.dumps(list(suppliers_all), cls=DjangoJSONEncoder)
# context = {'suppliers_all': suppliers_all,
# return HttpResponse(suppliers_all, content_type='application/json')


def display_jobs(request):
    jobs = Job.objects.all()
    context = {
        'jobs': jobs,
        'header': 'Job',
    }
    return render(request, 'display_jobs.html', context)


# def display_jobs(request):
#   jasonjobs = Job.objects.all()
#  jasonjobs = json.dumps({"data": list(jasonjobs)})
# data=serializers.serialize('data', jasonjobs)
# return render(HttpResponse, 'display_jobs.html', data)

# dataJason=list()
# context = {
#   'jobs': jobs,
#  'header': 'Job',
# }
# return render(request, 'display_jobs.html', context)


##def display_jobs_json(request):
##  alljobs= list (Job.objects.all())
##data = serializers.serialize('json', alljobs)
##return HttpResponse(data, content_type='application/json')


def display_jobs_json(request):
    data = [{
        'name': 'Vitor'
    }]
    return JsonResponse(data, safe=False)


# JOBS LIST VIEW FOR FILTER
# class JobsListView(ListView):
#   model = Job
#  template_name = 'JobListView.html'

# def get_context_data(self,**kwargs):
#     context = super().get_context_data(**kwargs)
#    context['filter'] = JobsFilter(self.request.GET , queryset=self.get_queryset())
#   return context


# def display_jobs(request):
#   data = list(Job.objects.values())

#  return JsonResponse(data, safe=False)


# DEPARTMENT VIEWS

# def display_active_jobs(request):
#   jobs = Job.objects.all().filter(job_status__icontains=)


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


class DepartmentAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Department.objects.all()

        if self.q:
            qs = qs.filter(department_name__istartswith=self.q)
        return qs


# ------ END USER VIEWS --------#

def department_view(request):
    departments = Department.objects.all()
    context = {
        'departments': departments,
        'header': 'Department',
    }
    return render(request, 'department_view.html', context)


def department_dashboard(request, id=None):
    instance = get_object_or_404(Department, id=id)
    assets = Equipment.objects.filter(department_id=instance)
    assets_count = Equipment.objects.filter(department_id=instance).count()
    jobs = Job.objects.filter(job_department_id=instance).exclude(job_final_status__contains='Completed')
    count_jobs_pending = Job.objects.filter(job_department_id=instance).exclude(
        job_final_status__contains='Completed').count()

    # next_ppm = Equipment.objects.filter(department_id=instance).filter(next_service_date__year=date.today().year)

    # delta = date.today() - date(Equipment.next_service_date)
    # ppm_days = delta.days

    # d0 = date.today()
    # d1 = Equipment.next_service_date
    # delta = d0 - d1
    # ppm_days = delta.days

    context = {
        'id': id,
        'instance': instance,
        'assets_count': assets_count,
        'assets': assets,
        'header': Equipment,
        'jobs': jobs,
        'count_jobs_pending': count_jobs_pending,

    }
    return render(request, 'department_dashboard.html', context)


def view_equipment(request, asset_id=None):
    instance = get_object_or_404(Equipment, asset_id=asset_id)
    equipment_jobs = Job.objects.all().filter(equipment=asset_id)
    context = {
        'asset_id': asset_id,
        'instance': instance,
        'equipment_jobs': equipment_jobs,
    }
    return render(request, "view_equipment.html", context)



# ------------------ Manufacturer Views ------------

def add_manufacturer(request):
    if request.method == "POST":
         form = ManufacturerForm(request.POST)
         if  form.is_valid():
              manufacturer = form.save()
              instance = manufacturer
              instance.save()
              form.save()
              return redirect('view_manufacturers')

    else:
      form = ManufacturerForm()
    return render(request, 'add_manufacturer.html', {'form': form})






def edit_manufacturer(request, id=None):
    instance = get_object_or_404(Manufacturer, id=id)
    form = ManufacturerForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance.save()
        return redirect('view_manufacturers')


    context = {
            "title": 'Edit ' + str(id),
            "instance": instance,
            "form": form,
            "id": id,

        }
    return render(request, "edit_manufacturer.html", context)


def view_manufacturers(request):
    manufacturers = Manufacturer.objects.all()
    context = {
        'manufacturers': manufacturers,
        'header': 'Manufacturer',
    }
    return render(request, 'view_manufacturers.html', context)


def add_model(request):
    if request.method == "POST":
         form = EquipmentModelForm(request.POST)
         if  form.is_valid():
              model = form.save()
              instance = model
              instance.save()
              form.save()
              return redirect('view_manufacturers')

    else:
      form = EquipmentModelForm()
    return render(request, 'add_model.html', {'form': form})
