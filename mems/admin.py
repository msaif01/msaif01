from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Equipment)
class ViewAdmin(ImportExportModelAdmin):
    pass

@admin.register(Job)
class ViewAdmin(ImportExportModelAdmin):
    pass

@admin.register(Manufacturer)
class ViewAdmin(ImportExportModelAdmin):
    pass

@admin.register(Department)
class ViewAdmin(ImportExportModelAdmin):
    pass


@admin.register(Category)
class ViewAdmin(ImportExportModelAdmin):
    pass

