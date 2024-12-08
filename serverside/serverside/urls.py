from django.contrib import admin
from django.urls import path
from mathapp import views 
urlpatterns = [
path('admin/', admin.site.urls), 
path('', views.EnergyCalc, name="EnergyCalc") # Root URL redirect
]