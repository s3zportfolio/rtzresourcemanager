from django import forms
from .models import EmployeeType


class EmpTypeForm(forms.ModelForm):
    class Meta:
        model=EmployeeType
        fields ='__all__'
