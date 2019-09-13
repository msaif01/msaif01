from django.conf.urls import url
from .views import*





urlpatterns = [
url(r'^$',index,name='index'),
url(r'^display_equipment$', display_equipment, name="display_equipment"),
url(r'^display_jobs$', display_jobs, name="display_jobs"),
url(r'^add_equipment$', add_equipment, name="add_equipment"),
url(r'^add_jobs$', add_jobs, name='add_jobs'),
url(r'^display_jobs/(?P<job_number>\d+)/$', job_edit, name='job_edit')
]