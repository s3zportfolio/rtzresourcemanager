from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def HomePage(request):
    return render(request,'homepage.html')
def MainMenu(request):
    return render(request,'mainpage.html')
