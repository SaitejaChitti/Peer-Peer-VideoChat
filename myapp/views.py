from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.utils.html import format_html
import requests


# Create your views here.
def home(request):
    return render(request,'index.html')
def base(request):
    return render(request,'base.html')

def register(request): 
    response1 = render(request, 'login.html')
    return response1
def register_user(request):
    if request.method=="POST":
            user_name=request.POST.get('logname')
            password=request.POST.get('logpass')
            email=request.POST.get('logemail')
            response = requests.post('http://localhost:5000/register',data={'username':user_name,'password':password,'email':email}).json()
            if 'error' in response.keys():
                messages.warning(request,response["error"])
                return redirect(register)
            messages.success(request,response["message"])
            return redirect(login)


def login(request):  
    return render(request, 'login.html')
def login_user(request):
    if request.method=="POST":
        username=request.POST.get('logname')
        password=request.POST.get('logpass')
        response = requests.post('http://localhost:5000/login',data={'username':username,'password':password}).json()
        if 'error' in response.keys():
            messages.warning(request,response["error"])
            return redirect(login)
        
        response1 = render(request, 'home.html', {})
        response1.set_cookie('username', username)
        print(response['message'])
        return response1
        

