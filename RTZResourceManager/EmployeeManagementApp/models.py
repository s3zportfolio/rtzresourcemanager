from django.db import models

# Create your models here.
class EmployeeType(models.Model):
    EmpTypeCode=models.CharField(primary_key=True,max_length=1)
    EmpType=models.CharField(max_length=30)
class EmployeeRole(models.Model):
    EmpRoleCode=models.CharField(primary_key=True,max_length=1)
    EmpRole=models.CharField(max_length=30)
class SalaryType(models.Model):
    SalaryCode=models.CharField(primary_key=True,max_length=1)
    SalType=models.CharField(max_length=30)
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
