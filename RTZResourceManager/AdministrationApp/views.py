from django.shortcuts import render
from .forms import EmpTypeForm

# Create your views here.
def home(request):
    return render(request,'index.html')
def employeelist(request):
    return render(request,'empList.html')
def employeetype(request):
    context={}
    form=EmpTypeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form']=form
    return render(request,'empType.html',context)
# Create your views here.
