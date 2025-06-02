from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import *
import uuid


# Create your views here.
def index(request):
    name=User.objects.get(id=1).username
    
    return render(request,'home.html',{'name':name})

def company(request):
    return render(request,'company.html')

def service(request):
    return render(request,'service.html')

def products(request):
    return render(request,'products.html')

def reviews(request):
    return render(request,'reviews.html')

def beds(request):
    # Fetching all furniture data from the database
    furniture_data = FurnitureData.objects.all
    return render(request, 'beds.html', {'beds': furniture_data})  # <-- Pass as 'beds'


def sofas(request):
    return render(request, 'sofas.html')

def loungechairs(request):
    return render(request, 'loungechairs.html')

def dressingtables(request):
    return render(request, 'dressingtables.html')

def wardrobes(request):
    return render(request, 'wardrobes.html')

def studytables(request):
    return render(request, 'studytables.html')

def diningtable(request):
    return render(request, 'diningtable.html')

def mattresses(request):
    return render(request, 'mattresses.html')

def bedpillows(request):
    return render(request, 'bedpillows.html')

def sofapillows(request):
    return render(request, 'sofapillows.html')

def shoerack(request):
    return render(request, 'shoerack.html')

def tvunit(request):
    return render(request, 'tvunit.html')

def cart(request):
    if request.method == 'POST':
        productmodel=request.POST['PRODUCTMODEL']
        name=request.POST['USERNAME']
        address=request.POST['ADDRESS']
        phoneno=request.POST['PHONENUMBER']
        try:
            BrightFurnitureUser.objects.create(productmodel=productmodel,name=name,address=address,phone=phoneno)
        except Exception as e:
            print("Your Order is Placed Successfully")
        return redirect('/')
    return render(request,'cart.html')

def contact(request):
    
    if request.method == 'POST':
        name=request.POST['USERNAME']
        email=request.POST['EMAIL']
        phoneno=request.POST['PHONENUMBER']
        message=request.POST['MESSAGE']
        try:
            user = BrightFurnitureUser.objects.get(name=name,email=email,phone=phoneno,message=message)
        except Exception as e:
            print("Your Message is Sent Successfully")
        return redirect('/')
    return render(request,'contact.html')

def delivery(request):
    return render(request,'delivery.html')

def interior(request):
    return render(request,'interior.html')

def assemblyservice(request):
    return render(request,'assemblyservice.html')

def warrantysupport(request):
    return render(request,'warrantysupport.html')

def emioptions(request):
    return render(request,'emioptions.html')

def checkout(request):
    if request.method == 'POST':
        productmodel = request.POST['PRODUCTMODEL']
        name = request.POST['USERNAME']
        address = request.POST['ADDRESS']
        phoneno = request.POST['PHONENUMBER']
        try:
            BrightFurnitureUser.objects.create(productmodel=productmodel, name=name, address=address, phone=phoneno)
        except Exception as e:
            print("Your Order is Placed Successfully")
        return redirect('/')
    return render(request, 'checkout.html')

def joinUS(request):
    print(request.POST)
    return render(request,'joinUS.html')
