from django.db import models

# Create your models here.

class Equipment(models.Model):

 assetId = models.AutoField(max_length=6, primary_key=True)
 serialNumber = models.CharField(max_length=10,default='')
 manufacturer = models.CharField(max_length=10,default='')
 category = models.CharField(max_length=10,default='')
 department = models.CharField(max_length=10,default='')
 purchaseOrder= models.CharField(max_length=10,default='')

def __str__(self):
        return 'assetId : {0} serialNumber : {1} manufacturer : {2} category : {3} department : {4} purchaseOrder'.format(self.assetId, self.serialNumber, self.manufacturer ,self.category, self.department, self.purchaseOrder)

