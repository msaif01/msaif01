from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.

class EquipmentResource(resources.ModelResource):
    class Meta:
        model = Equipment
        fields = ('asset_id, serial_number, category, manufacturer, model, department, purchase_order, cost, accepted_date, warranty_expiry, equipment_status, next_service_date')
        exclude = ('asset_id')


@admin.register(Equipment)
class ViewAdmin(ImportExportModelAdmin):
    resource_class = EquipmentResource

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

@admin.register(Model)
class ViewAdmin(ImportExportModelAdmin):
    pass