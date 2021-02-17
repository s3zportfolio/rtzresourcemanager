<<<<<<< HEAD
from django.shortcuts import render,redirect,HttpResponseRedirect
=======
from django.shortcuts import render,redirect
>>>>>>> ebed649da7331c595821be34f065f19cbfa64872
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
<<<<<<< HEAD

            #return redirect('empType.html')
    else:
        form=EmpTypeForm()
    #return render(request,'empType.html',{'form':form})
    allEmpTypes=EmployeeType.objects.all()
    return render(request,'empType.html',{
        'form':form,
      'allEmpTypes':allEmpTypes
      })
=======
    #return render(request,'empType.html',{'form':form})
    allEmpTypes=EmployeeType.objects.all()
    return render(request,'empType.html',{
      'allEmpTypes':allEmpTypes,
      'form':form,
      })
#def ListEmployeeType(request):
#    allEmpTypes=EmployeeType.objects.all()
#    return render(request,'empType.html',{'allEmpTypes':allEmpTypes})
# Create your views here.
>>>>>>> ebed649da7331c595821be34f065f19cbfa64872
