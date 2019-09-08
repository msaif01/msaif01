from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def index(request):
    return render(request,'index.html')

# Create your views here.
def display_equipment(request):
    items = Equipment.objects.all()
    context = {
        'items': items,
        'header': 'Equipment',
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
        return render(request, 'add_equipment.html', {'form' : form})


def add_equipment(request):
    return add_item(request, EquipmentForm)

