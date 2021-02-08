from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def employeedetails(request):
    return render(request,'empDetails.html')
# Create your views here.
