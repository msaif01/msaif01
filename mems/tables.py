import django_tables2 as tables
from .models import Job

class JobsTable(tables.Table):
    class Meta:
        model = Job
template_name = "django_tables2/bootstrap4.html"