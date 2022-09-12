from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'signup.html')

def booking(request):
    return render(request,'booking.html')

def login(request):
    return render(request,'login.html')

def cusotmer_rend(request):
    customer = Customer.objects.all()
    tour = Tour.objects.all()
    loc = Loc.objects.all()
    guide = Guide.objects.all()
    spot = Spot.objects.all()
    model = Model.objects.all()
    car = Car.objects.all()
    context = {'customer':customer,'tour':tour,'loc':loc,
        'guide':guide,'spot':spot,'model':model,'car':car
    }
    return render(request,'user-data.html',context)