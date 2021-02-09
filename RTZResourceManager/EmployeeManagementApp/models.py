from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
    empId=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    dateofbirth=models.DateTimeField()
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=30)
    address=models.CharField(max_length=500)
    employeetype=models.CharField(max_length=1)
    salarytype=models.CharField(max_length=1)
    startdate=models.DateTimeField()
    enddate=models.DateTimeField()
