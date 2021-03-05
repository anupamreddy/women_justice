from django.shortcuts import render
from django.contrib.auth import	authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from account.models import victim

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


"""
def police_login(request):
    if request.method == 'GET':
        return render(request,'police_login.html')
"""
def signup(request):
    if request.method == 'GET':
        return render(request,'victim_signup.html')    

@login_required
def dashboard(request):
    return render(request,'dashboard.html',{'section':'dashboard'})          
