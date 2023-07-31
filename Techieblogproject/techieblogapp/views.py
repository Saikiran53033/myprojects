from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):

    uname = request.POST.get('uname')
    pwd = request.POST.get('password1')
    repwd = request.POST.get('password2')
    email = request.POST.get('email')
    phno = request.POST.get('phonenumber')

    if request.method == "POST":

        if pwd != repwd:
            return HttpResponse("Password is not matching Re-enter password")
        else:
            user =  User.objects.create_user(uname, email,pwd)
            user.save()
            return redirect('signin')

    return render(request=request, template_name='register.html')

def signin(request):

    username = request.POST.get('uname')
    password = request.POST.get('password')

    user = authenticate(request=request, username = username, password = password)

    if user is not None:

        login(request, user)
        return redirect('home')

    return render(request=request, template_name='signin.html')

@login_required
def homepage(request):

    return render(request=request, template_name='homepage.html')

def cover(request):

    return render(request=request, template_name='coverpage.html',)


def logout(request):

    logout(request)

    return redirect('signin')