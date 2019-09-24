from django.conf.urls import url
from .views import*





urlpatterns = [
url(r'^$',display_equipment,name='index'),
url(r'^display_equipment$', display_equipment, name="display_equipment"),
url(r'^display_jobs$', display_jobs, name="display_jobs"),
url(r'^add_equipment$', add_equipment, name="add_equipment"),
url(r'^add_jobs$', add_jobs, name='add_jobs'),
url(r'^edit_job/(?P<job_number>\d+)/$', edit_job, name='edit_job'),
url(r'^job_view/(?P<job_number>\d+)/$', job_view, name='job_view'),
url(r'^JobListView$',JobsListView.as_view()),
url(r'^manufacturer-autocomplete/$',ManufacturerAutocomplete.as_view(), name='manufacturer-autocomplete',),
url(r'^equipment-autocomplete/$',EquipmentAutocomplete.as_view(), name='equipment-autocomplete',),
]