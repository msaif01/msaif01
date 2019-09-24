from import_export import resources
from .models import*

class EquipmentResource(resources.ModelResource):
    class Meta:
        model = Equipment
        exclude = ('asset_id')