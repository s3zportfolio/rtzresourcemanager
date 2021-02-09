from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
    EmpId=models.IntegerField(primary_key=True)
    First_Name=models.CharField(max_length=45)
    Last_Name=models.CharField(max_length=45)
    DateofBirth=models.DateTimeField()
    Email=models.CharField(max_length=200)
    Phone=models.CharField(max_length=30)
    Address=models.CharField(max_length=500)
    EmployeeType=models.CharField(max_length=1)
    EmployeeRole=models.CharField(max_length=1)
    SalaryType=models.CharField(max_length=1)
    StartDate=models.DateTimeField()
    EndDate=models.DateTimeField()
