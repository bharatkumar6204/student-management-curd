from django.shortcuts import render,redirect
from .models import Student

# Create your views here.

def home(request):
    std=Student.objects.all()
    return render(request, 'home.html', {'std':std})

def add_std(request):
    if request.method=='POST':
        #retreive the user input
        stds_name=request.POST.get("name")
        stds_roll=request.POST.get("roll")
        stds_email=request.POST.get("email")
        stds_address=request.POST.get("address")
        stds_phone=request.POST.get("phone")

        #create an object for models
        s=Student()
        s.name=stds_name
        s.roll=stds_roll
        s.email=stds_email
        s.address=stds_address
        s.phone=stds_phone
        s.save()
        return redirect('home')
    return render(request, 'add_std.html')

def delete_std(request,roll):
    s=Student.objects.get(pk=roll)
    s.delete()
    return redirect('home')

def update_std(request, roll):
    s = Student.objects.get(pk=roll)
    return render(request, 'update.html', {'s': s})

def do_update_std(request, roll):
    if request.method == 'POST':
        std_name = request.POST.get('std_name')
        std_roll = request.POST.get('std_roll')
        std_email = request.POST.get('std_email')
        std_address = request.POST.get('std_address')
        std_phone = request.POST.get('std_phone')

        s = Student.objects.get(pk=roll)
        s.name = std_name
        s.roll = std_roll
        s.email = std_email
        s.address = std_address
        s.phone = std_phone
        s.save()

        return redirect('home')
    