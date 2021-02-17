from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='index'),
    path('administration/EmpList',views.employeelist,name='employeelist'),
    path('administration/EmpType',views.employeetype,name='employeetype'),




]
