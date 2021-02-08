from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='index'),
    path('employeedetails/',views.employeedetails,name='employeedetails')
]
