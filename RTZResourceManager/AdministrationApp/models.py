from django.db import models

class EmployeeType(models.Model):
    EmpTypeCode=models.CharField(primary_key=True,max_length=1)
    EmpType=models.CharField(max_length=30)
class EmployeeRole(models.Model):
    EmpRoleCode=models.CharField(primary_key=True,max_length=1)
    EmpRole=models.CharField(max_length=30)
class SalaryType(models.Model):
    SalaryCode=models.CharField(primary_key=True,max_length=1)
    SalType=models.CharField(max_length=30)

# Create your models here.
