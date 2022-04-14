from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request,'index.html') 

def login(request):
    context = {
        'form':loginForm(),
        "type":"login"
    }
    return render(request, 'login.html', context=context)    

def signup(request):
    if request.method == "POST":
        signup_form = signupForm(request.POST)
        password = request.POST.get('password')
        if signup_form.is_valid():
            user = signup_form.save(commit=False)
            user.set_password(password)
            user.save()
            return redirect("login")
        else:
            print(signup_form.errors)
    context = {
        'form':signupForm(),
        "type":"signup"
    }
    return render(request, 'login.html', context=context)    

def package(request):
    context = {
        "tourPackages": TourPackage.objects.all()
    }
    return render(request,'tour_pakage.html', context=context)   

def services(request):

    return render(request,'services.html') 

def contact(request):

    return render(request,'contact.html') 

def help(request):

    return render(request,'help.html') 

def record(request):
    
    return render(request,'record.html') 

def home(request):
    
    return render(request,'home.html') 

def tour(request):

    return render(request,'Tour_location.html')

def place(request,tour_id):
    context = {
        "places": VisitPlaces.objects.filter(package=TourPackage.objects.get(id=tour_id)),
        "package":TourPackage.objects.get(id=tour_id)
    }
    return render(request, 'place.html', context=context)