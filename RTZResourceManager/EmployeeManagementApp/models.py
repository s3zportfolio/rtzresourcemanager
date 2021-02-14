from django.db import models
from AdministrationApp.models import EmployeeType, EmployeeRole, SalaryType

# Create your models here.

class EmployeeInformation(models.Model):
    EmpId=models.IntegerField(primary_key=True)
    First_Name=models.CharField(max_length=45)
    Last_Name=models.CharField(max_length=45)
    DateofBirth=models.DateTimeField()
    Email=models.CharField(max_length=200)
    Phone=models.CharField(max_length=30)
    Address=models.CharField(max_length=500)
    EmployeeType=models.ForeignKey(EmployeeType,to_field='EmpTypeCode',on_delete=models.CASCADE)
    Role=models.ForeignKey(EmployeeRole,to_field='EmpRoleCode',on_delete=models.CASCADE)
    SalaryType=models.ForeignKey(SalaryType,to_field='SalaryCode',on_delete=models.CASCADE)
    StartDate=models.DateTimeField()
    EndDate=models.DateTimeField()
