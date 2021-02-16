from django import forms
from .models import EmployeeType


class EmpTypeForm(forms.ModelForm):
    class Meta:
        model=EmployeeType
        fields = ['EmpTypeCode','EmpType']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'
