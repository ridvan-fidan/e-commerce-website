from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def userRegister(request):
    form = UserForm()
    if request.method == "POST":
       form = UserForm(request.POST) 
       if form.is_valid():
           form.save()
           return redirect('login')
    context = {
        'form':form
    }
    return render(request, 'register.html',context)

def userLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username =username , password = password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return redirect('login')

    return render (request, 'login.html')
