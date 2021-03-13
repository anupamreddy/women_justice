from django.shortcuts import render
from django.contrib.auth import	authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import victim,police,case,pol_case,vic_case 
from random import randint
from django.db.models.aggregates import Count

# Create your views here.
def home_page(request):
    return render(request,'index.html')

def victim_login(request):
    if request.method == 'GET':
        return render(request,'victim_login')
    elif request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        try :
            victim_object = victim.objects.get()
        except :
            print("No such user exists")
            return render(request,'victim_login', context={'error': 'No such user exists'})
        
        if victim_object.password == password :
            request.session['member_id'] = victim_object.id
            return render(request, 'dashboard')
        else:
            print("our username and password didn't match")
            return render(request,'victim_login', context={'error': 'our username and password does not match'})


def victim_logout(request) :
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return render(request, '/')

def file_case(request):
    if request.method == 'GET':
        return render(request,'file_case.html')
    else:
        descreption=request.POST['descreption']
        area = request.POST['area']

        count = police.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        case_head=police.objects.filter(police_station=area,is_head=True).all()[random_index] 

        filed_case=case.objects.create(descreption=descreption,police_station=area)

        pol_case.objects.create(case=filed_case,police=case_head)


"""
def police_login(request):
    if request.method == 'GET':
        return render(request,'police_login.html')
"""
def signup(request):
    if request.method == 'GET':
        return render(request,'victim_signup.html')
    else:
        name=request.POST['uname']
        password=request.POST['psw']
        if(victim.objects.filter(name=name)):
            print("user name should be unique")
        else:
            victim.objects.create(name=name,password=password)
            print("created successfully")
            return render(request,'victim_login.html')

@login_required
def dashboard(request):
    return render(request,'dashboard.html',{'section':'dashboard'})          
