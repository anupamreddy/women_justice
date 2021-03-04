from django.shortcuts import render
from django.contrib.auth import	authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page(request):
    return render(request,'index.html')

def victim_login(request):
    if request.method == 'GET':
        return render(request,'victim_login.html')

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