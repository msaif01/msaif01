import itertools

from django.db import models
import datetime
from django.urls import reverse
from django.utils.datetime_safe import date
from datetime import timedelta,timezone
from dateutil.relativedelta import relativedelta





class Person(models.Model):
    person_name = models.CharField(max_length=40, default=1)
    def __str__(self):
        return self.person_name



class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=100)
    manufacturer_email = models.CharField(null=True, max_length=100)
    manufacturer_number = models.CharField(null=True, max_length=50)

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

#class Stock(models.Model):
 #  stock_number = models.CharField(max_length=50)
  # stock_description = models.CharField(max_length=50)
   #stock_price = models.FloatField()
   #stock_quantity = models.IntegerField()

   #def __str__(self):
    #  return 'STOCK ID:{0}    DESCRIPTION:{1}    PRICE:'.format(self.stock_number, self.stock_description,self.stock_price)


class Category(models.Model):

    CATEGORY_RISK_SCORE_CHOICES = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]

    category_name = models.CharField(max_length=50)
    category_risk_score = models.IntegerField(choices=CATEGORY_RISK_SCORE_CHOICES)
    category_depreciation_factor = models.IntegerField(default=7)

    def __str__(self):
        return self.category_name

    class Meta:
        ordering = ["category_name"]

class Model(models.Model):
    model_name = models.CharField(max_length=60, default='')
    model_manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model_description =  models.CharField(max_length=100, default='')
    model_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    model_price = models.IntegerField()

    def __str__(self):
        return self.model_name
    class Meta:
        ordering = ["model_name"]



class Equipment(models.Model):

    blank = ''
    active = 'Active'
    decommusioned = 'Decommusioned'
    lost = 'Lost'
    ppm_due = 'PPM due'

    EQUIPMENT_STATUS_CHOICES = [
        (active, 'Active'),
        (decommusioned, 'Decommusioned'),
        (lost, 'Lost'),
        (ppm_due,'PPM Due')]

    asset_id = models.AutoField(primary_key=True)
    serial_number = models.CharField(max_length=25, default='', help_text="Enter Serial Number")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, default=1)
    model = models.ForeignKey(Model, on_delete=models.CASCADE,default=1)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,default=1)
    risk_score = models.IntegerField(default=3)
    ppm_intervel = models.IntegerField(default=365)
    cost = models.IntegerField()
    purchase_order = models.CharField(max_length=25, default='')
    accepted_date = models.DateField("Accepted On", default=date.today)
    warranty_expiry = models.DateField("Warranty Expiry")
    equipment_status = models.CharField(max_length=20,choices=EQUIPMENT_STATUS_CHOICES, default='ACTIVE')
    service_date = models.DateField("Serviced on", default=date.today)
    next_service_date = models.DateField("PPM Due", default=date.today)
    ppm_due_days = models.IntegerField("PPM Due in Days", default=365)
    ppm_due_months = models.IntegerField("PPM due in Months", default=12)

    #'@property
    #def get_risk_score(self):
     # r = self.category.category_risk_score+self.department.department_risk_score
      #return r

    #@property
    #def get_ppm_intervel(self):
     #   if self.risk_score >  8  :
      #     p = 180
       # else : p = 365
        #return p


    #@property
    #def get_next_service_date(self):
     #   n = self.service_date + datetime.timedelta(days=self.ppm_intervel)
      #  return n

    #@property
    #def get_ppm_due_days(self):
     #   delta = (self.next_service_date - self.service_date).days
      #  pp = delta
       # return pp




    #@property
    #def save(self, *args, **kwargs):

      #self.risk_score = self.get_risk_score
      #self.ppm_intervel = self.get_ppm_intervel
      #self.next_service_date = self.get_next_service_date
      #self.ppm_due_days = self.get_ppm_due_days
      #super(Equipment, self).save(*args, **kwargs)






    def __str__(self):
      return '{0}'.format(self.asset_id)

       #return 'asset_id : {0} serial_number : {1} category : {2} manufacturer : {3} model : {4}  department : {5} purchase_order : {6} accepted_date :{7} warranty_expiry : {8} equipment_status : {9} service_date :{10} next_service_date'.format(
        #self.asset_id, self.serial_number, self.category,self.manufacturer, self.model, self.department, self.purchase_order,self.accepted_date,self.warranty_expiry,self.equipment_status,self.service_date,self.next_service_date)


class Service(models.Model):
    asset_id = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    serviced_on = models.DateField()

    def __str__(self):
       return '{0}'.format(self.asset_id)

def generatejob():
    return itertools.count(start=1450, step=1)


class Job(models.Model):
    from datetime import date

    blank = ''
    acceptance = 'Acceptance'
    acceptance_loan = 'Acceptance (Loan)'
    ppm = 'PPM'
    repair = 'Repair'
    incident = 'Incident'
    supply = 'Supply'
    training = 'Training'

    JOB_TYPE_CHOICES = [
        (blank,''),
        (acceptance, 'Acceptence'),
        (acceptance_loan, 'Acceptence Loan'),
        (ppm, 'PPM'),
        (repair, 'Repair'),
        (incident, 'Incident'),
        (supply, 'Supply'),
        (training,'Training')]


    reported = 'Reported'
    created = 'Created'
    in_progress = 'In-progress'
    in_progress_ad = 'In-progress Awaiting diagnosis'
    in_progress_am = 'In-progress Awaiting manufacturer'
    in_progress_ap = 'In-progress Awaiting parts'


    JOB_STATUS_CHOICES = [
        (reported, 'Reported'),
        (created, 'Created'),
        (in_progress, 'In progress'),
        (in_progress_ad , 'In-progress Awaiting diagnosis'),
        (in_progress_am , 'In-progress Awaiting manufacturer'),
        (in_progress_ap , 'In-progress Awaiting parts'),
    ]



    abandoned = 'Abandoned'
    completed = 'Completed'

    JOB_FINAL_STATUS_CHOUCES = [
        (abandoned,'Abandoned'),
        (completed, 'Completed'),
    ]

    completed_acceptance = 'Completed Acceptence'
    completed_repair = 'Completed Repair'
    completed_service = 'Completed Service'
    completed_= 'Completed Service'
    n_completed_condemned = 'Not Completed - Equipment Condemned'

    JOB_OUTCOME = [
        (completed_acceptance, 'Completed Acceptence'),
        (completed_repair, 'Completed Repair'),
        (completed_service, 'Completed Service'),
        (completed_, 'Completed Service'),
        (n_completed_condemned , 'Not Completed - Equipment Condemned'),
    ]




    JOB_WORKDONE_TIME_CHOICES = [(15,'15'),(30,'30'),(45,'45'),(60,'60'),(90,'90'),(120,'120'),(180,'180'),(240,'240')]

    job_number = models.AutoField(primary_key=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE,blank=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, default='Repair')
    job_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    job_status = models.CharField(max_length=40, choices=JOB_STATUS_CHOICES, default='CREATED')
    job_final_status = models.CharField(max_length=40,choices=JOB_FINAL_STATUS_CHOUCES,default='')
    job_outcome = models.CharField(max_length=40,choices=JOB_OUTCOME,default='')
    job_date = models.DateField("Job created on", default=date.today)
    job_finished_date = models.DateField("Job finished on", default=date.today)
    job_description = models.CharField(max_length=100, default='')
    job_work_done = models.TextField(max_length=300, default='',blank=True)
    job_service_done = models.BooleanField(default=False)
    job_time_taken = models.IntegerField(choices=JOB_WORKDONE_TIME_CHOICES, default=0)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, default=1)
    job_sheet = models.FileField(blank=True)
    #stock = models.ForeignKey(Stock, on_delete=models.CASCADE)

    def natural_key(self):
        return self.my_natural_key

  #  def save(self, *args, **kwargs):

   #     if self.job_service_done == 'TRUE':
    #        self.equipment.service_date = self.job_finished_date
     #       super().save(**kwargs)

    def __str__(self):
        return 'job_number : {0} equipment : {1} job_department : {2} job_type : {3} job_status : {4} job_description : {5} job_work_done : {6} job_service_done : {7} person_name: {8} job_time_taken : {9} job_final_status :'.format(
        self.job_number, self.equipment, self.job_department, self.job_type, self.job_status, self.job_description, self.job_work_done,self.job_service_done, self.person, int(self.job_time_taken),self.job_final_status)



