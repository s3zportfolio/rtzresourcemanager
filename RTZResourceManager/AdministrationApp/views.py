from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import EmpTypeForm
from .models import EmployeeType

# Create your views here.
def home(request):
    return render(request,'index.html')
def employeelist(request):
    return render(request,'empList.html')
def employeetype(request):
    if request.method=='POST':
        form=EmpTypeForm(request.POST)
        if form.is_valid():
            form.save()
            form=EmpTypeForm()

            #return redirect('empType.html')
    else:
        form=EmpTypeForm()
    #return render(request,'empType.html',{'form':form})
    allEmpTypes=EmployeeType.objects.all()
    return render(request,'empType.html',{
        'form':form,
      'allEmpTypes':allEmpTypes
      })
