from django.contrib import admin
from django.urls import path
from myhome import views

urlpatterns = [

    path("",views.index,name='home'),
    path("login",views.login,name='login'),
    path("signup",views.signup,name='signup'),
    path("tour",views.package,name='tour_pakage'),
    path("place/<tour_id>",views.place,name='place'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
    path("help",views.help,name='help'),
    path("record",views.record,name='record'),
    path("home",views.home,name='home'),
    path("location",views.tour,name='tour_location')
]
   