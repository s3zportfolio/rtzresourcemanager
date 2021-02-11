from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def employeelist(request):
    return render(request,'empList.html')
def employeetype(request):
    return render(request,'empType.html')
# Create your views here.
