from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='index'),
    path('HomePage/',views.HomePage,name='homepage'),
    path('MainMenu/',views.MainMenu, name='mainmenu')
]
