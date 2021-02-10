from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def employeelist(request):
    return render(request,'empList.html')
# Create your views here.
