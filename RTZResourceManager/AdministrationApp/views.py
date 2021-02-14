from django.shortcuts import render
from .forms import EmpTypeForm

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
            return redirect('empType.html')
    else:
            form=EmpTypeForm()
    return render(request,'empType.html',{'form':form})

# Create your views here.
