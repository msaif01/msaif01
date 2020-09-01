from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponseRedirect
from mems.models import Manufacturer
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.views import View
from django.views.generic import ListView,DetailView
from .tables import JobsTable
from .filters import JobsFilter
from dal import autocomplete
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.db.models import Count

def index(request):
    return render(request, 'index.html')

# Create your views here.




# ----------------VIEWS RELATED TO EQUIPMENT MODEL

def display_equipment(request):
    equipments = Equipment.objects.all()
    context = {
        'equipments': equipments,
        'header': Equipment,
    }
    return render(request, 'EquipmentView.html', context)

def add_equipment(request):
    if request.method == "POST":
        form = EquipmentForm(request.POST)

        if form.is_valid():
            equipment=form.save(commit=False)
            equipment.save()
            instance = equipment
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
        instance = form.save(commit=False)
        instance.save()
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
          form.save()
          instance = job
          if job.job_status == 'Serviced':
              job.equipment.service_date = job.job_date

          return redirect('view_job', instance.job_number)

    else:
        form = JobsForm()
    return render(request, 'add_jobs.html', {'form': form})


def edit_job(request, job_number=None):
    instance = get_object_or_404(Job, job_number=job_number)
    form = JobsForm(request.POST or request.FILES  or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        form.save()
        instance.save()

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
    instance.job_cost = (instance.job_time_taken*1)
    context = {
        'job_number': job_number,
        'instance': instance,
    }
    return render(request, "view_job.html", context)

#def display_jobs_json(request):
 #   jsonjobs=list(Job.objects.values())
  #  return JsonResponse(jsonjobs, safe=False)




#def display_jobs_json(request):
 #   jsonjobs = Job.objects.all()
  #  jsonjobs = json.dumps(list(jsonjobs), cls=DjangoJSONEncoder)

   # context = {'jsonjobs': jsonjobs,
             #  'header': Job}
    #return HttpResponse(jsonjobs, content_type='application/json')

#def supjson(request):
 #   suppliers_all = Supplier.objects.all().values('name', 'classification')
  #  suppliers_all = json.dumps(list(suppliers_all), cls=DjangoJSONEncoder)
   # context = {'suppliers_all': suppliers_all,
    #return HttpResponse(suppliers_all, content_type='application/json')



def display_jobs(request):
    jobs = Job.objects.all()
    context = {
        'jobs': jobs,
        'header': 'Job',
    }
    return render(request, 'display_jobs.html', context)


#def display_jobs(request):
 #   jasonjobs = Job.objects.all()
  #  jasonjobs = json.dumps({"data": list(jasonjobs)})
   # data=serializers.serialize('data', jasonjobs)
    #return render(HttpResponse, 'display_jobs.html', data)

    #dataJason=list()
    #context = {
     #   'jobs': jobs,
      #  'header': 'Job',
    #}
    #return render(request, 'display_jobs.html', context)




##def display_jobs_json(request):
  ##  alljobs= list (Job.objects.all())
    ##data = serializers.serialize('json', alljobs)
    ##return HttpResponse(data, content_type='application/json')



def display_jobs_json(request):
    data =[{
        'name': 'Vitor'
    }]
    return JsonResponse(data, safe=False)


# JOBS LIST VIEW FOR FILTER
#class JobsListView(ListView):
 #   model = Job
  #  template_name = 'JobListView.html'

   # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
     #    context['filter'] = JobsFilter(self.request.GET , queryset=self.get_queryset())
      #   return context






#def display_jobs(request):
 #   data = list(Job.objects.values())

  #  return JsonResponse(data, safe=False)


# DEPARTMENT VIEWS

#def display_active_jobs(request):
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
    jobs = Job.objects.filter(job_department_id=instance).exclude(job_status__icontains='Completed').count()

    context = {
        'id': id,
        'instance': instance,
        'assets_count': assets_count,
        'assets': assets,
        'header': Equipment,
        'jobs': jobs,
    }
    return render(request, 'department_dashboard.html',context)




def view_equipment(request, asset_id=None):
    instance = get_object_or_404(Equipment, asset_id=asset_id)
    equipment_jobs = Job.objects.all().filter(equipment=asset_id)
    context = {
        'asset_id': asset_id,
        'instance': instance,
        'equipment_jobs': equipment_jobs,
    }
    return render(request, "view_equipment.html", context)