from django.conf.urls import url
from django.conf.urls.static import static
from .views import*
from django.conf import settings




urlpatterns = [
url(r'^$',index,name='index'),
url(r'^display_equipments$', display_equipments, name="display_equipments"),
url(r'^display_jobs', display_jobs, name="display_jobs"),

url(r'^display_jobs_json/$', display_jobs_json, name="display_jobs_json"),
url(r'^add_equipment$', add_equipment, name="add_equipment"),
url(r'^view_equipment/(?P<asset_id>\d+)/$', view_equipment, name='view_equipment'),
url(r'^edit_equipment/(?P<asset_id>\d+)/$', edit_equipment, name='edit_equipment'),

url(r'^add_jobs$', add_jobs, name='add_jobs'),
url(r'^edit_job/(?P<job_number>\d+)/$', edit_job, name='edit_job'),
url(r'^view_job/(?P<job_number>\d+)/$', view_job, name='view_job'),


url(r'^department_view$', department_view, name="department_view"),
url(r'^department_dashboard/(?P<id>\d+)/$', department_dashboard, name="department_dashboard"),
#url(r'^JobListView$',JobsListView.as_view()),


url(r'^manufacturer-autocomplete/$',ManufacturerAutocomplete.as_view(), name='manufacturer-autocomplete',),
url(r'^equipment-autocomplete/$',EquipmentAutocomplete.as_view(), name='equipment-autocomplete',),
url(r'^department-autocomplete/$',DepartmentAutocomplete.as_view(), name='department-autocomplete',),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

