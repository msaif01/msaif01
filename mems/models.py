from django.db import models
import datetime
from django.urls import reverse


# Create your models here.


class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=30)
    manufacturer_email = models.CharField(max_length=100)
    manufacturer_number = models.CharField(max_length=30)
    manufacturer_address = models.TextField()

    def __str__(self):
        return self.manufacturer_name

    class Meta:
        ordering = ["manufacturer_name"]


class Department(models.Model):

    DEPARTMENT_RISK_SCORE_CHOICES = [(1, '1'), (2, '2'), (3, '3')]

    department_name = models.CharField(max_length=30)
    department_email = models.CharField(max_length=100)
    department_number = models.CharField(max_length=30)
    department_location = models.TextField()
    department_costCode = models.CharField(max_length=30)
    department_risk_score = models.IntegerField(choices=DEPARTMENT_RISK_SCORE_CHOICES)

    def __str__(self):
        return self.department_name
    class Meta:
        ordering = ["department_name"]


class Category(models.Model):

    CATEGORY_RISK_SCORE_CHOICES = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]

    category_name = models.CharField(max_length=50)
    category_risk_score = models.IntegerField(choices=CATEGORY_RISK_SCORE_CHOICES)

    def __str__(self):
        return self.category_name

    class Meta:
        ordering = ["category_name"]


class Equipment(models.Model):
    asset_id = models.AutoField(max_length=6, primary_key=True)
    serial_number = models.CharField(max_length=25, default='')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    purchase_order = models.CharField(max_length=25, default='')

    def __str__(self):
        return '{0}'.format(self.asset_id)
       # return 'asset_id : {0} serial_number : {1} manufacturer : {2} category : {3} department : {4} purchase_order'.format(
        #    self.asset_id, self.serial_number, self.manufacturer, self.category, self.department, self.purchase_order)



class Job(models.Model):
    from datetime import date


    acceptance = 'Acceptance'
    acceptance_loan = 'Acceptance (Loan)'
    ppm = 'PPM'
    repair = 'Repair'
    incident = 'Incident'
    supply = 'Supply'

    JOB_TYPE_CHOICES = [
        (acceptance, 'Acceptence'),
        (acceptance_loan, 'Acceptence Loan'),
        (ppm, 'PPM'),
        (repair, 'Repair'),
        (incident, 'Incident'),
        (supply, 'Supply')]

    JOB_TYPE_CHOICES = [
        (acceptance, 'Acceptence'),
        (acceptance_loan, 'Acceptence Loan'),
        (ppm, 'PPM'),
        (repair, 'Repair'),
        (incident, 'Incident'),
        (supply, 'Supply'),
    ]

    created = 'Created'
    in_progress = 'In progress'
    completed_acceptance = 'Completed (Acceptance)'
    completed_service = 'Completed (Service)'
    completed_repair =  'Completed (Repair)'
    completed_repair_service = 'Completed (Repair & Service)'

    JOB_STATUS_CHOICES = [
        (created, 'Created'),
        (in_progress, 'In progress'),
        (completed_acceptance, 'Completed Acceptance'),
        (completed_service, 'Completed Service'),
        (completed_repair, 'Completed Repair'),
        (completed_repair_service, 'Completed Repair and Service')
    ]

    JOB_WORKDONE_TIME_CHOICES = [(15,'15'),(30,'30'),(45,'45'),(60,'60'),(90,'90'),(120,'120'),(180,'180'),(240,'240')]

    job_number = models.AutoField(max_length=6, primary_key=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    job_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    job_status = models.CharField(max_length=20, choices=JOB_STATUS_CHOICES)
    job_date = models.DateField("Date", default=date.today)
    job_description = models.CharField(max_length=100, default='')
    job_work_done = models.CharField(max_length=300, default='')
    job_time_taken = models.IntegerField(choices=JOB_WORKDONE_TIME_CHOICES, default=0)


    def __str__(self):
        return 'job_number : {0} equipment : {1} job_department : {2} job_type : {3} job_status : {4} job_description : {5} job_work_done'.format(
            self.job_number, self.equipment, self.job_department, self.job_type, self.job_status, self.job_description, self.job_work_done)



class Stock(models.Model):
    stock_number = models.CharField(max_length=20)
    stock_description= models.CharField(max_length=50)
    stock_price = models.IntegerField()
    stock_quantity = models.IntegerField()

