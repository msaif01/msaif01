from django.conf.urls import url
from .views import*





urlpatterns = [
url(r'^$',index,name='index'),
url(r'^display_equipment$', display_equipment, name="display_equipment"),
url(r'^add_equipment$', add_equipment, name="add_equipment"),

]