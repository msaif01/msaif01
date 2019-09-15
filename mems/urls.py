from django.conf.urls import url
from .views import*





urlpatterns = [
url(r'^$',display_equipment,name='index'),
url(r'^display_equipment$', display_equipment, name="display_equipment"),
url(r'^display_jobs$', display_jobs, name="display_jobs"),
url(r'^add_equipment$', add_equipment, name="add_equipment"),
url(r'^add_jobs$', add_jobs, name='add_jobs'),
url(r'^job_edit/(?P<job_number>\d+)/$', job_edit, name='job_edit'),
url(r'^job_view/(?P<job_number>\d+)/$', job_view, name='job_view'),
url(r'^simple_list$', table_view, name='table_view')
]