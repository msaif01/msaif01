from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Equipment)
class ViewAdmin(admin.ModelAdmin):
    pass

@admin.register(Job)
class ViewAdmin(admin.ModelAdmin):
    pass

@admin.register(Manufacturer)
class ViewAdmin(admin.ModelAdmin):
    pass

@admin.register(Department)
class ViewAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class ViewAdmin(admin.ModelAdmin):
    pass

