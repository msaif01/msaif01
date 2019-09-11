from django.db import models


# Create your models here.

class Equipment(models.Model):
    assetId = models.AutoField(max_length=6, primary_key=True)
    serialNumber = models.CharField(max_length=25, default='')
    manufacturer = models.CharField(max_length=40, default='')
    category = models.CharField(max_length=25, default='')
    department = models.CharField(max_length=25, default='')
    purchaseOrder = models.CharField(max_length=25, default='')
    def __str__(self):
        return 'assetId : {0} serialNumber : {1} manufacturer : {2} category : {3} department : {4} purchaseOrder'.format(
        self.assetId, self.serialNumber, self.manufacturer, self.category, self.department, self.purchaseOrder)


class Job(models.Model):
    acceptance = 'acceptance'
    acceptance_loan = 'acceptance_loan'
    ppm = 'ppm'
    repair = 'repair'
    incident = 'incident'
    supply = 'supply'


    JOB_TYPE_CHOICES = [
        (acceptance, 'Acceptence'),
        (acceptance_loan, 'Acceptence Loan'),
        (ppm, 'PPM'),
        (repair, 'Repair'),
        (incident, 'Incident'),
        (supply, 'supply')]



    JOB_TYPE_CHOICES = [
        (acceptance, 'Acceptence'),
        (acceptance_loan, 'Acceptence Loan'),
        (ppm, 'PPM'),
        (repair, 'Repair'),
        (incident, 'Incident'),
        (supply, 'Supply'),
    ]

    created = 'created'
    in_progress = 'in_progress'
    completed_service = 'completed_service'
    completed_repair = 'completed_repair'
    completed_repairservice = 'completed_repairservice'

    JOB_STATUS_CHOICES = [
        (created, 'Created'),
        (in_progress, 'In progress'),
        (completed_service, 'Completed Service'),
        (completed_repair, 'Completed Repair'),
        (completed_repairservice, 'Completed Repair and Service')
    ]

    job_number = models.AutoField(max_length=6, primary_key=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    job_type = models.CharField(max_length=20,choices=JOB_TYPE_CHOICES)
    job_status = models.CharField(max_length=20,choices=JOB_STATUS_CHOICES)
    job_description = models.CharField(max_length=100, default='')
    job_work_done = models.CharField(max_length=300, default='')

    def __str__(self):
        return 'job_number : {0} equipment : {1} job_type : {2} job_status : {3} job_description : {4} job_work_done'.format(
        self.job_number, self.equipment, self.job_type, self.job_status, self.job_description, self.job_work_done)





